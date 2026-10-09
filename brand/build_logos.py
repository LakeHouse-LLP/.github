"""LakeHouse Studio brand kit v0.3: the locked L1 mark, lockups, app icon, favicons,
social preview, README header and brand board -> final/.
v0.3 = taste-skill pass (design-taste-frontend v2): Geist/Geist Mono, no em-dashes, accent only in the mark.
Run: python3 build_tokens.py && python3 build_logos.py
Needs: cairosvg, Pillow, fontTools, uharfbuzz; fonts Geist and Geist Mono (OFL).
All text is converted to outlines, so the SVGs render the same everywhere.
Old directions A-D: archive/directions-v0/. Previous kit (v0.2, Fraunces/Inter): archive/final-v1/."""
import json, math, base64, io, os
import cairosvg, uharfbuzz as hb
from PIL import Image
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

OUT='/workspace/lakehouse-brand'; FIN=f'{OUT}/final'; PNG=f'{FIN}/png'
os.makedirs(PNG,exist_ok=True)
T=json.load(open(f'{OUT}/tokens.json'))
def tok(*path):
    v=T
    for p in path: v=v[p]
    v=v['$value']
    if isinstance(v,str):  # alias {color.palette.x.y}
        return tok(*v.strip('{}').split('.'))
    return v['hex'].upper()
PAL=T['color']['palette']
C=dict(bg=tok('color','bg','canvas'), surface=tok('color','bg','surface'), raised=tok('color','bg','raised'),
       overlay=tok('color','bg','overlay'), sunken=tok('color','bg','sunken'), border=tok('color','border','subtle'),
       ink=tok('color','logo','ink'), accent=tok('color','accent'), muted=tok('color','text','secondary'),
       faint=tok('color','text','muted'), mono=tok('color','logo','mono'))

# ---------------------------------------------------------------- the L1 mark
# 120-unit grid. Letter tops all sit on one gable line y = 0.75*|x-60| (pitch 3:4, ~36.9 deg).
# L = stem + foot; the old glass panel is now a void. H = two stems + bar. Baseline y=113.
# Horizon line: full mark width (flush), gap 6, thickness 5 (thickened only at tiny sizes).
L_PATH='M0 45 L26 25.5 V89 H56 V113 H0 Z'
H_PATH='M64 3 L82 16.5 V65 H102 V31.5 L120 45 V113 H102 V83 H82 V113 H64 Z'
BASE=113
def mark(ink, line, lt=5, gap=6):
    return (f'<path d="{L_PATH}" fill="{ink}"/><path d="{H_PATH}" fill="{ink}"/>'
            f'<rect x="0" y="{BASE+gap}" width="120" height="{lt}" fill="{line}"/>')
def mark_box(lt=5,gap=6): return (0,3,120,BASE+gap+lt)   # x0,y0,x1,y1
def geom_for(px, units):
    """Line thickness/gap for a render where `units` grid units span `px` pixels.
    Keeps the line >=1.5 px and the gap >=1 px at tiny sizes; design values otherwise."""
    u=px/units
    return max(5, math.ceil(1.5/u)), max(6, math.ceil(1.0/u))

def svg(w,h,body,vb=None,title='LakeHouse Studio'):
    vb=vb or f'0 0 {w} {h}'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{vb}" role="img" aria-label="{title}">'
            f'<title>{title}</title>{body}</svg>\n')
def save(name, s): open(f'{FIN}/{name}','w').write(s)
def png(s, path, w, h=None): cairosvg.svg2png(bytestring=s.encode(), write_to=path, output_width=w, output_height=h or w)

def mark_svg(px, variant='dark', margin=20, lt=None, gap=None):
    """Square mark. variant: dark (on #1E1E1E), transparent, mono, mono-reversed."""
    size=120+2*margin
    if lt is None: lt,gap=geom_for(px,size)
    x0,y0,x1,y1=mark_box(lt,gap); cy=(y0+y1)/2
    vb=f'{60-size/2:g} {cy-size/2:g} {size:g} {size:g}'
    ink,line={'dark':(C['ink'],C['accent']),'transparent':(C['ink'],C['accent']),
              'mono':(C['mono'],C['mono']),'mono-reversed':(C['ink'],C['ink'])}[variant]
    bg=f'<rect x="{60-size/2-1:g}" y="{cy-size/2-1:g}" width="{size+2:g}" height="{size+2:g}" fill="{C["bg"]}"/>' if variant=='dark' else ''
    return svg(px,px,bg+mark(ink,line,lt,gap),vb,f'LakeHouse Studio mark ({variant})')

def tile_svg(px, S=216, rx_ratio=0.2237, lt=None, gap=None, title='LakeHouse Studio app icon'):
    """Rounded-square tile (#1E1E1E). S = tile size in grid units (mark is 120 wide)."""
    if lt is None: lt,gap=geom_for(px,S)
    x0,y0,x1,y1=mark_box(lt,gap); cy=(y0+y1)/2
    vb=f'{60-S/2:g} {cy-S/2:g} {S:g} {S:g}'
    body=(f'<rect x="{60-S/2:g}" y="{cy-S/2:g}" width="{S:g}" height="{S:g}" rx="{S*rx_ratio:.2f}" fill="{C["bg"]}"/>'
          + mark(C['ink'],C['accent'],lt,gap))
    return svg(px,px,body,vb,title)

# ---------------------------------------------------------------- text to outlines
G_DIR='/usr/share/fonts/truetype/sand-box/google'
FONTS={'geist':f'{G_DIR}/Geist/Geist-VariableFont_wght.ttf',
       'mono':f'{G_DIR}/Geist Mono/GeistMono-VariableFont_wght.ttf'}
_hb={}
def _font(key,var):
    k=(key,tuple(sorted(var.items())))
    if k not in _hb:
        face=hb.Face(hb.Blob.from_file_path(FONTS[key])); f=hb.Font(face)
        if var: f.set_variations(var)
        _hb[k]=(f,face.upem)
    return _hb[k]
def text(s, key, size, wght=400, track=0.0, x=0, y=0, anchor='start', fill='#fff'):
    """Shape with HarfBuzz (kerning on), return (svg <path>, advance width, bbox). y = baseline, track in em."""
    f,upem=_font(key,{'wght':wght}); sc=size/upem
    buf=hb.Buffer(); buf.add_str(s); buf.guess_segment_properties(); hb.shape(f,buf,{'kern':True,'liga':True})
    adv=0; glyphs=[]; n=len(buf.glyph_infos)
    for i,(gi,gp) in enumerate(zip(buf.glyph_infos,buf.glyph_positions)):
        glyphs.append((gi.codepoint, adv+gp.x_offset, gp.y_offset)); adv+=gp.x_advance+(track*upem if i<n-1 else 0)
    width=adv*sc
    ox={'start':0,'middle':-width/2,'end':-width}[anchor]+x
    pen=SVGPathPen(None); bp=BoundsPen(None)
    for gid,gx,gy in glyphs:
        m=(sc,0,0,-sc,ox+gx*sc,y-gy*sc)
        f.draw_glyph_with_pen(gid,TransformPen(pen,m)); f.draw_glyph_with_pen(gid,TransformPen(bp,m))
    return f'<path d="{pen.getCommands()}" fill="{fill}"/>', width, bp.bounds or (ox,y,ox,y)
_,_,_b=text('H','geist',1000,600); CAP=(_b[3]-_b[1])/1000     # Geist cap-height ratio
def tw(s,key,size,wght=400,track=0.0): return text(s,key,size,wght,track)[1]

# ---------------------------------------------------------------- wordmark + lockups
# Wordmark: "LakeHouse" Geist SemiBold + "Studio" Geist Regular in text.secondary, one line, tracking -1%.
def wordmark(x, baseline, cap, ink, sub, anchor='start'):
    size=cap/CAP; tr=-0.01
    w1=tw('LakeHouse','geist',size,600,tr); sp=tw(' ','geist',size,400); w2=tw('Studio','geist',size,400,tr)
    total=w1+sp+w2; x0={'start':x,'middle':x-total/2,'end':x-total}[anchor]
    p1,_,_=text('LakeHouse','geist',size,600,tr,x=x0,y=baseline,fill=ink)
    p2,_,_=text('Studio','geist',size,400,tr,x=x0+w1+sp,y=baseline,fill=sub)
    return p1+p2,(x0,baseline-cap,x0+total,baseline)
H_CAP,H_BASE,H_GAP=44,92,40          # horizontal lockup: cap 44 units, cap block centered on the letters' mass
def lockup_parts(ink,line,sub,kind):
    m=mark(ink,line)
    if kind=='horizontal':
        wm,b=wordmark(120+H_GAP,H_BASE,H_CAP,ink,sub); box=(0,3,b[2],124)
    else:
        wm,b=wordmark(60,124+44+30,30,ink,sub,anchor='middle'); box=(min(0,b[0]),3,max(120,b[2]),b[3])
    return m+wm,box
def lockup(variant, kind):
    ink,line,sub,bg={'dark':(C['ink'],C['accent'],C['muted'],C['bg']),'transparent':(C['ink'],C['accent'],C['muted'],None),
                     'mono':(C['mono'],C['mono'],C['mono'],None),'mono-reversed':(C['ink'],C['ink'],C['ink'],None)}[variant]
    body,(x0,y0,x1,y1)=lockup_parts(ink,line,sub,kind)
    pad=28; w=x1-x0+2*pad; h=y1-y0+2*pad
    vb=f'{x0-pad:.1f} {y0-pad:.1f} {w:.1f} {h:.1f}'
    bgr=f'<rect x="{x0-pad-1:.1f}" y="{y0-pad-1:.1f}" width="{w+2:.1f}" height="{h+2:.1f}" fill="{bg}"/>' if bg else ''
    W=1024 if kind=='horizontal' else 640
    return svg(W,round(W*h/w),bgr+body,vb,f'LakeHouse Studio logo ({kind}, {variant})'), (w,h)

# ---------------------------------------------------------------- build
SIZES=[16,32,64,128,256,512,1024]
files=[]
for v in ('dark','transparent','mono','mono-reversed'):
    name='lakehouse-mark.svg' if v=='dark' else f'lakehouse-mark-{v}.svg'
    save(name, mark_svg(1024,v,lt=5,gap=6)); files.append(name)
save('lakehouse-appicon.svg', tile_svg(1024,lt=5,gap=6)); files.append('lakehouse-appicon.svg')
for px in SIZES:
    tight= px<=48   # tiny sizes: tighter margin so the letters get more pixels
    for v in ('dark','transparent'):
        png(mark_svg(px,v,margin=8 if tight else 20), f'{PNG}/mark-{v}-{px}.png', px)
    png(mark_svg(px,'mono',margin=8 if tight else 20), f'{PNG}/mark-mono-{px}.png', px)
    png(tile_svg(px,S=150 if tight else 216, rx_ratio=0.2 if tight else 0.2237), f'{PNG}/appicon-{px}.png', px)
# favicons: tile with small margin, line thickened per size
fav={}
for px in (16,32,48):
    s=tile_svg(px,S=146,rx_ratio=0.18,title='LakeHouse Studio'); p=f'{FIN}/favicon-{px}.png'; png(s,p,px); fav[px]=Image.open(p).convert('RGBA')
save('favicon.svg', tile_svg(32,S=146,rx_ratio=0.18,lt=7,gap=6,title='LakeHouse Studio').replace('width="32" height="32" ',''))
fav[48].save(f'{FIN}/favicon.ico', sizes=[(16,16),(32,32),(48,48)], append_images=[fav[16],fav[32]])
save('favicon-mono.svg', mark_svg(32,'mono',margin=8,lt=7,gap=6).replace('width="32" height="32" ',''))
for kind in ('horizontal','stacked'):
    for v in ('dark','transparent','mono','mono-reversed'):
        s,(w,h)=lockup(v,kind); name=f'lakehouse-lockup-{kind}.svg' if v=='dark' else f'lakehouse-lockup-{kind}-{v}.svg'
        save(name,s)
        for W in (512,1024,2048): png(s,f'{PNG}/lockup-{kind}-{v}-{W}w.png',W,round(W*h/w))

# ---------------------------------------------------------------- shared copy (taste pass: no em-dashes, <=20-word subtext)
TAG1,TAG2='A second home for','your design practice.'
SUB1,SUB2='Revit and Rhino tools, production helpers and','office admin for small design practices.'
URL='github.com/LakeHouse-LLP'
def place(body,x,y,sc): return f'<g transform="translate({x:g} {y:g}) scale({sc:g})">{body}</g>'

# social preview 1280x640: asymmetric split. Left: brand strip, headline, subtext, URL (4 text elements).
# Right: the mark, large. Accent appears only in the mark's horizon line.
def social():
    b=[f'<rect width="1280" height="640" fill="{C["bg"]}"/>']
    wm,_=wordmark(96,120,20,C['ink'],C['muted']); b.append(wm)
    for i,l in enumerate((TAG1,TAG2)):
        t,_,_=text(l,'geist',64,600,-0.02,x=93,y=292+i*74,fill=C['ink']); b.append(t)
    for i,l in enumerate((SUB1,SUB2)):
        t,_,_=text(l,'geist',24,400,x=96,y=428+i*36,fill=C['muted']); b.append(t)
    t,_,_=text(URL,'mono',18,400,x=96,y=548,fill=C['faint']); b.append(t)
    sc=2.6; b.append(place(mark(C['ink'],C['accent']),1280-96-120*sc,320-63.5*sc,sc))
    return svg(1280,640,''.join(b),title='LakeHouse Studio social preview')

# README header 1280x320: left-aligned stack, mark + wordmark + one line of tagline; open space on the right.
def header():
    b=[f'<rect width="1280" height="320" fill="{C["bg"]}"/>']
    sc=1.5; b.append(place(mark(C['ink'],C['accent']),80,160-63.5*sc,sc))
    x=80+120*sc+48
    wm,_=wordmark(x,150,34,C['ink'],C['muted']); b.append(wm)
    t,_,_=text(TAG1+' '+TAG2,'geist',24,400,x=x,y=198,fill=C['muted']); b.append(t)
    return svg(1280,320,''.join(b),title='LakeHouse Studio')
for n,f,w,h in (('social-preview',social,1280,640),('readme-header',header,1280,320)):
    s=f(); save(f'{n}.svg',s); png(s,f'{FIN}/{n}.png',w,h)

# ---------------------------------------------------------------- brand board 1600x1200
# brandkit-style 2+2+2 grid with uneven panel weights: quiet cover, technical construction,
# tagline, digital application, color proportions, type. No per-panel eyebrows, one radius (12), 24 px gutters.
def img_tag(path,x,y,w,h):
    d=base64.b64encode(open(path,'rb').read()).decode()
    return f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="data:image/png;base64,{d}"/>'
def board():
    W,H,M,GU=1600,1200,64,24
    b=[f'<rect width="{W}" height="{H}" fill="{C["sunken"]}"/>']
    def panel(x,y,w,h,fill): b.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}"/>')
    def T(*a,**k): t,w,bb=text(*a,**k); b.append(t); return w
    # header: one line, no version stamp
    w1=T('LakeHouse Studio','geist',26,600,-0.01,x=M,y=96,fill=C['ink'])
    T('Brand kit, October 2026','geist',18,400,x=M+w1+16,y=96,fill=C['faint'])
    top=136; colL=968; colR=W-2*M-colL-GU; xR=M+colL+GU
    # A1 cover
    yA,hA=top,440; panel(M,yA,colL,hA,C['bg'])
    body,(x0,y0,x1,y1)=lockup_parts(C['ink'],C['accent'],C['muted'],'horizontal'); sc=1.0
    b.append(place(body,M+88,yA+hA/2-(y0+y1)/2*sc,sc))
    # A2 construction
    panel(xR,yA,colR,hA,C['bg']); sc=2.0; cx=xR+colR/2; cy=yA+hA/2+4
    ox,oy=cx-60*sc,cy-63.5*sc
    for gx in range(0,121,20):
        b.append(f'<path d="M{ox+gx*sc:.1f} {yA+40} V{yA+hA-40}" stroke="{C["surface"]}" stroke-width="1"/>')
    b.append(place(mark(C['ink'],C['accent']),ox,oy,sc))
    def U(x,y): return ox+x*sc, oy+y*sc
    (ax,ay),(px,py),(bx,by)=U(-14,55.5),U(60,0),U(134,55.5)
    b.append(f'<path d="M{ax:.1f} {ay:.1f} L{px:.1f} {py:.1f} L{bx:.1f} {by:.1f}" fill="none" stroke="{C["faint"]}" stroke-width="1" stroke-dasharray="4 4"/>')
    (l0,ly),(l1,_)=U(-14,113),U(134,113)
    b.append(f'<path d="M{l0:.1f} {ly:.1f} H{l1:.1f}" stroke="{C["faint"]}" stroke-width="1" stroke-dasharray="4 4"/>')
    T('pitch 3:4','mono',12,400,x=px+16,y=py-10,fill=C['faint'])
    T('baseline','mono',12,400,x=l0-8,y=ly+4,anchor='end',fill=C['faint'])
    T('120 units, line 5, gap 6','mono',12,400,x=cx,y=yA+hA-36,anchor='middle',fill=C['faint'])
    # B1 tagline (bottom-left anchored, open space above)
    yB,hB=yA+hA+GU,300; wB1=584; panel(M,yB,wB1,hB,C['bg'])
    for i,l in enumerate((TAG1,TAG2)): T(l,'geist',40,600,-0.02,x=M+46,y=yB+hB-104+i*50,fill=C['ink'])
    # B2 digital application: browser tab + app icons
    xB2=M+wB1+GU; wB2=W-M-xB2; panel(xB2,yB,wB2,hB,C['surface'])
    bx0,by0,bw=xB2+48,yB+48,476
    b.append(f'<rect x="{bx0}" y="{by0}" width="{bw}" height="100" rx="12" fill="{C["raised"]}"/>')
    b.append(f'<path d="M{bx0+12} {by0+0.5} H{bx0+bw-12}" stroke="#FFFFFF" stroke-opacity="0.06"/>')
    b.append(f'<rect x="{bx0+10}" y="{by0+10}" width="220" height="36" rx="8" fill="{C["overlay"]}"/>')
    b.append(img_tag(f'{FIN}/favicon-16.png',bx0+24,by0+20,16,16))
    T('LakeHouse Studio','geist',13,500,x=bx0+50,y=by0+33,fill=C['ink'])
    b.append(f'<rect x="{bx0+10}" y="{by0+54}" width="{bw-20}" height="36" rx="8" fill="{C["bg"]}"/>')
    T(URL,'mono',13,400,x=bx0+26,y=by0+77,fill=C['faint'])
    for px,(ix,iy) in zip((48,32,16),((bx0,yB+hB-48-48),(bx0+72,yB+hB-48-32),(bx0+128,yB+hB-48-16))):
        b.append(img_tag(f'{FIN}/favicon-{px}.png',ix,iy,px,px))
    T('favicon at 48, 32, 16 px','mono',12,400,x=bx0+160,y=yB+hB-50,fill=C['faint'])
    b.append(img_tag(f'{PNG}/appicon-256.png',xB2+wB2-48-176,yB+(hB-176)/2,176,176))
    # C1 color proportions (accent kept to a sliver on purpose)
    yC,hC=yB+hB+GU,H-M-(yB+hB+GU); panel(M,yC,colL,hC,C['bg'])
    bands=[('sunken',C['sunken'],10),('canvas',C['bg'],32),('surface',C['surface'],18),('raised',C['raised'],12),('overlay',C['overlay'],9),('ink',C['ink'],13),('accent',C['accent'],6)]
    sx,sy,sw,sh=M+48,yC+40,colL-96,92; x=sx
    b.append(f'<clipPath id="strip"><rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="8"/></clipPath><g clip-path="url(#strip)">')
    pos=[]
    for n,c,p in bands:
        w=sw*p/100; b.append(f'<rect x="{x:.1f}" y="{sy}" width="{w+0.6:.1f}" height="{sh}" fill="{c}"/>'); pos.append((n,c,x,w)); x+=w
    b.append('</g>')
    b.append(f'<rect x="{sx+0.5}" y="{sy+0.5}" width="{sw-1}" height="{sh-1}" rx="8" fill="none" stroke="{C["border"]}"/>')
    for n,c,x,w in pos:
        last=n=='accent'
        T(c.upper(),'mono',12,400,x=(x+w if last else x+8),y=sy+sh+26,anchor='end' if last else 'start',fill=C['faint'])
    # C2 type
    panel(xR,yC,colR,hC,C['surface'])
    T('Aa','geist',104,600,-0.02,x=xR+44,y=yC+hC-52,fill=C['ink'])
    T('Geist','geist',18,600,x=xR+228,y=yC+76,fill=C['ink']); T('display and UI','geist',14,400,x=xR+228,y=yC+98,fill=C['faint'])
    T('Geist Mono','mono',18,500,x=xR+228,y=yC+140,fill=C['ink']); T('code and data','geist',14,400,x=xR+228,y=yC+162,fill=C['faint'])
    return svg(W,H,''.join(b),title='LakeHouse Studio brand board')
s=board(); save('brand-board.svg',s); png(s,f'{FIN}/brand-board.png',1600,1200)
print('done')
