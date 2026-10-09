"""Writes tokens.json (W3C DTCG 2025.10 format) and contrast-table.md. Dark mode only.
v0.2 (2026-10-09): surfaces moved from night-blue to neutral graphite greys (canvas #1E1E1E); logo = L1 mark.
v0.3 (2026-10-09, taste-skill pass): pure-neutral grey ramp with even steps, near-neutral text, no pure black,
Geist + Geist Mono instead of Fraunces/Inter, room colors removed (one accent), design dials recorded.
To change the brand accent, edit ACCENT (+ hover/pressed) here, re-run, and every alias follows."""
import json
from contrast import cr
ACCENT, ACCENT_HOVER, ACCENT_PRESSED = '#7DFFFF', '#B3FFFF', '#4FE0E6'
def col(h, d=None):
    h=h.lstrip('#'); t={"$type":"color","$value":{"colorSpace":"srgb","components":[round(int(h[i:i+2],16)/255,4) for i in (0,2,4)],"hex":"#"+h.lower()}}
    if d: t["$description"]=d
    return t
def ref(p,d=None,typ="color"):
    t={"$type":typ,"$value":"{"+p+"}"}
    if d: t["$description"]=d
    return t
dim=lambda v,u="px":{"$type":"dimension","$value":{"value":v,"unit":u}}
dur=lambda v:{"$type":"duration","$value":{"value":v,"unit":"ms"}}
PAL={
 # neutral dark greys, like pro design software (Figma/Blender/VS Code). canvas = graphite.900
 # one grey family, pure neutral (R=G=B), even ~8-step elevation ramp. canvas = graphite.900 (locked)
 "graphite":{"950":"#161616","900":"#1E1E1E","850":"#262626","800":"#2E2E2E","750":"#383838","700":"#474747","600":"#8F8F8F"},
 "stone":{"500":"#73716D","400":"#AAA8A4","300":"#C7C5C0","100":"#F2EFE9","0":"#FFFFFF"},
 "lake":{"600":"#2C6488","500":"#3A7CA5","400":"#5E9BC2","300":"#8DB8D2","200":"#B9D5E5"},
 "timber":{"700":"#7A4A26","500":"#A8693A","300":"#D4A373","200":"#E6C49F"},
 "dusk":{"500":"#E8875A","300":"#F0A98A"},
 "reed":{"300":"#7FD1A0"},"amber":{"300":"#F2C46D"},"coral":{"300":"#FF8A80"},
}
color={"accent":col(ACCENT,"THE brand accent. Single source of truth; everything references this. Use on dark surfaces only: links, focus, key highlights, primary button fill."),
       "accent-hover":col(ACCENT_HOVER,"Lighter accent for hover. Re-derive if color.accent changes."),
       "accent-pressed":col(ACCENT_PRESSED,"Deeper accent for pressed/active. Re-derive if color.accent changes."),
       "palette":{k:{s:col(v) for s,v in d.items()} for k,d in PAL.items()}}
color["bg"]={"canvas":ref("color.palette.graphite.900","App/page background"),"surface":ref("color.palette.graphite.850","Cards, panels, sidebars"),
             "raised":ref("color.palette.graphite.800","Menus, popovers, hovered rows"),"overlay":ref("color.palette.graphite.750","Dialogs, toasts"),
             "sunken":ref("color.palette.graphite.950","Wells, code blocks, canvas viewports"),
             "accent":ref("color.accent","Primary button fill"),"accent-subtle":{"$type":"color","$value":{"colorSpace":"srgb","components":[0.4902,1,1],"alpha":0.12,"hex":"#7dffff"},"$description":"12% accent tint for selected rows/chips (keep in sync with color.accent)"}}
color["text"]={"primary":ref("color.palette.stone.100"),"secondary":ref("color.palette.stone.300"),"muted":ref("color.palette.stone.400","Captions, metadata"),
               "disabled":ref("color.palette.stone.500","Disabled only; exempt from 4.5:1"),"link":ref("color.accent"),"on-accent":ref("color.palette.graphite.900","Text/icons on accent fills"),
               "brand-warm":ref("color.palette.timber.300","Warm highlights in illustration and charts, never UI chrome")}
color["border"]={"subtle":ref("color.palette.graphite.700","Dividers (decorative)"),"strong":ref("color.palette.graphite.600","Input/control outlines, needs >=3:1"),"focus":ref("color.accent")}
color["border"]["highlight"]={"$type":"color","$value":{"colorSpace":"srgb","components":[1,1,1],"alpha":0.06,"hex":"#ffffff"},"$description":"1 px inner top edge on raised/overlay surfaces. Replaces drop-shadow glow."}
color["data"]={str(i+1):ref(p) for i,p in enumerate(["color.accent","color.palette.timber.300","color.palette.lake.300","color.palette.dusk.300","color.palette.reed.300","color.palette.stone.300"])}
color["data"]["$description"]="Categorical chart order. Charts only; never UI chrome."
color["status"]={"success":ref("color.palette.reed.300"),"warning":ref("color.palette.amber.300"),"danger":ref("color.palette.coral.300"),"info":ref("color.palette.lake.300")}
color["logo"]={"ink":ref("color.palette.stone.100","Letters of the L1 mark"),"horizon-line":ref("color.accent","The thin horizon line under the letters"),"mono":ref("color.palette.graphite.900","Mono logo on unavoidable light grounds"),"mono-reversed":ref("color.palette.stone.100","Single-ink logo on photos/video"),"tile":ref("color.palette.graphite.900","App icon / favicon tile")}
font={"family":{"display":{"$type":"fontFamily","$value":["Geist","Segoe UI Variable Display","SF Pro Display","system-ui","sans-serif"]},
                "sans":{"$type":"fontFamily","$value":["Geist","Segoe UI Variable Text","SF Pro Text","system-ui","sans-serif"]},
                "mono":{"$type":"fontFamily","$value":["Geist Mono","ui-monospace","Cascadia Mono","Consolas","monospace"]},
                "cjk":{"$type":"fontFamily","$value":["Noto Sans SC","Source Han Sans SC","PingFang SC","Microsoft YaHei","sans-serif"]}},
      "weight":{k:{"$type":"fontWeight","$value":v} for k,v in dict(regular=400,medium=500,semibold=600,bold=700).items()}}
scale=[("display",48,52,"display","semibold",-1.2),("h1",36,42,"display","semibold",-0.7),("h2",28,34,"display","semibold",-0.3),("h3",22,30,"sans","semibold",0),
       ("h4",18,26,"sans","semibold",0),("body-lg",17,28,"sans","regular",0),("body",15,24,"sans","regular",0),("body-sm",13,20,"sans","regular",0),
       ("caption",12,16,"sans","medium",0.2),("label",12,16,"sans","medium",0.2),("code",13,20,"mono","regular",0)]
font["size"]={n:dim(s) for n,s,*_ in scale}
typography={n:{"$type":"typography","$value":{"fontFamily":"{font.family.%s}"%f,"fontSize":"{font.size.%s}"%n,"fontWeight":"{font.weight.%s}"%w,
            "letterSpacing":{"value":ls,"unit":"px"},"lineHeight":round(lh/s,3)}} for n,s,lh,f,w,ls in scale}
space={str(k):dim(v) for k,v in {0:0,1:2,2:4,3:8,4:12,5:16,6:24,7:32,8:48,9:64,10:96}.items()}
radius={k:dim(v) for k,v in dict(none=0,sm=4,md=8,lg=12,xl=16,full=9999).items()}
def sh(y,b,a,sp=0): return {"color":{"colorSpace":"srgb","components":[0.0392,0.0392,0.0392],"alpha":a,"hex":"#0a0a0a"},"offsetX":{"value":0,"unit":"px"},"offsetY":{"value":y,"unit":"px"},"blur":{"value":b,"unit":"px"},"spread":{"value":sp,"unit":"px"}}
shadow={"sm":{"$type":"shadow","$value":sh(1,2,0.5)},"md":{"$type":"shadow","$value":sh(4,12,0.55)},"lg":{"$type":"shadow","$value":sh(12,32,0.6)},
        "$description":"Secondary cue only. Elevation = a lighter surface step + border.highlight. Shadow color is off-black #0A0A0A, never pure black."}
motion={"duration":{"instant":dur(0),"fast":dur(120),"base":dur(200),"slow":dur(320),"calm":dur(480)},
        "easing":{"standard":{"$type":"cubicBezier","$value":[0.2,0,0,1]},"enter":{"$type":"cubicBezier","$value":[0,0,0,1]},"exit":{"$type":"cubicBezier","$value":[0.3,0,1,1]},"ripple":{"$type":"cubicBezier","$value":[0.4,0,0.2,1]}}}
DIALS={"DESIGN_VARIANCE":5,"MOTION_INTENSITY":3,"VISUAL_DENSITY":3,"VISUAL_DENSITY_product_ui":5,
       "$description":"taste-skill (design-taste-frontend v2) dials. Calm, professional, architectural home office."}
tokens={"$extensions":{"studio.lakehouse.dials":DIALS},"$description":"LakeHouse Studio design tokens v0.3.0. Dark mode only (explicit brand decision). W3C Design Tokens (DTCG 2025.10). Source for packages/design-tokens.",
        "color":color,"font":font,"typography":typography,"space":space,"radius":radius,"shadow":shadow,"motion":motion,
        "size":{"control":{"sm":dim(28),"md":dim(36),"lg":dim(44)},"icon":{"sm":dim(16),"md":dim(20),"lg":dim(24)},"focus-ring":dim(2),"hit-target-min":dim(24)}}
json.dump(tokens,open('tokens.json','w'),indent=2,ensure_ascii=False)
# contrast table
P={**{f"graphite.{k}":v for k,v in PAL['graphite'].items()},**{f"stone.{k}":v for k,v in PAL['stone'].items()}}
G=PAL["graphite"]
bgs=[("bg.sunken",G["950"]),("bg.canvas",G["900"]),("bg.surface",G["850"]),("bg.raised",G["800"]),("bg.overlay",G["750"])]
fgs=[("text.primary","#F2EFE9"),("text.secondary",PAL["stone"]["300"]),("text.muted",PAL["stone"]["400"]),("text.disabled",PAL["stone"]["500"]),("accent / text.link",ACCENT),("accent-hover",ACCENT_HOVER),("accent-pressed",ACCENT_PRESSED),
     ("lake.300 (info)","#8DB8D2"),("lake.400","#5E9BC2"),("timber.300","#D4A373"),("dusk.300","#F0A98A"),("reed.300 (success)","#7FD1A0"),("amber.300 (warning)","#F2C46D"),("coral.300 (danger)","#FF8A80"),("border.strong",G["600"]),("border.subtle",G["700"])]
def g(r): return "AAA" if r>=7 else "AA" if r>=4.5 else "3:1 UI/large" if r>=3 else "decorative only"
L=["| Foreground | Hex | "+" | ".join(f"{n} `{h}`" for n,h in bgs)+" |","|---|---|"+"---|"*len(bgs)]
for n,h in fgs: L.append(f"| {n} | `{h}` | "+" | ".join(f"{cr(h,b):.2f} {g(cr(h,b))}" for _,b in bgs)+" |")
L+=["","| Pair | Ratio | Rating |","|---|---|---|"]
for a,an,b,bn in [(G["900"],"text.on-accent (graphite.900)",ACCENT,"bg.accent"),(G["900"],"graphite.900 text",ACCENT_HOVER,"accent-hover fill"),(G["900"],"graphite.900 text",ACCENT_PRESSED,"accent-pressed fill"),(G["900"],"graphite.900 text","#F0A98A","dusk.300 fill"),(G["900"],"mono logo ink","#FFFFFF","white (light contexts)"),(ACCENT,"accent","#FFFFFF","white (NOT allowed)"),(ACCENT,"accent","#F2EFE9","stone.100 (NOT allowed)")]:
    r=cr(a,b); L.append(f"| {an} `{a}` on {bn} `{b}` | {r:.2f}:1 | {g(r) if 'NOT' not in bn else 'fail, never use'} |")
open('contrast-table.md','w').write("\n".join(L)+"\n")
print("\n".join(L))
