| Foreground | Hex | bg.sunken `#161616` | bg.canvas `#1E1E1E` | bg.surface `#262626` | bg.raised `#2E2E2E` | bg.overlay `#383838` |
|---|---|---|---|---|---|---|
| text.primary | `#F2EFE9` | 15.77 AAA | 14.53 AAA | 13.19 AAA | 11.83 AAA | 10.22 AAA |
| text.secondary | `#C7C5C0` | 10.49 AAA | 9.67 AAA | 8.77 AAA | 7.87 AAA | 6.80 AA |
| text.muted | `#AAA8A4` | 7.62 AAA | 7.02 AAA | 6.38 AA | 5.72 AA | 4.94 AA |
| text.disabled | `#73716D` | 3.72 3:1 UI/large | 3.42 3:1 UI/large | 3.11 3:1 UI/large | 2.79 decorative only | 2.41 decorative only |
| accent / text.link | `#7DFFFF` | 15.18 AAA | 13.99 AAA | 12.70 AAA | 11.39 AAA | 9.84 AAA |
| accent-hover | `#B3FFFF` | 16.08 AAA | 14.82 AAA | 13.45 AAA | 12.07 AAA | 10.42 AAA |
| accent-pressed | `#4FE0E6` | 11.32 AAA | 10.43 AAA | 9.47 AAA | 8.50 AAA | 7.34 AAA |
| lake.300 (info) | `#8DB8D2` | 8.55 AAA | 7.87 AAA | 7.15 AAA | 6.41 AA | 5.54 AA |
| lake.400 | `#5E9BC2` | 5.98 AA | 5.51 AA | 5.00 AA | 4.49 3:1 UI/large | 3.88 3:1 UI/large |
| timber.300 | `#D4A373` | 8.00 AAA | 7.37 AAA | 6.69 AA | 6.00 AA | 5.18 AA |
| dusk.300 | `#F0A98A` | 9.26 AAA | 8.53 AAA | 7.74 AAA | 6.95 AA | 6.00 AA |
| reed.300 (success) | `#7FD1A0` | 9.94 AAA | 9.15 AAA | 8.31 AAA | 7.46 AAA | 6.44 AA |
| amber.300 (warning) | `#F2C46D` | 11.11 AAA | 10.23 AAA | 9.29 AAA | 8.34 AAA | 7.20 AAA |
| coral.300 (danger) | `#FF8A80` | 7.93 AAA | 7.30 AAA | 6.63 AA | 5.95 AA | 5.14 AA |
| border.strong | `#8F8F8F` | 5.60 AA | 5.15 AA | 4.68 AA | 4.20 3:1 UI/large | 3.63 3:1 UI/large |
| border.subtle | `#474747` | 1.95 decorative only | 1.79 decorative only | 1.63 decorative only | 1.46 decorative only | 1.26 decorative only |

| Pair | Ratio | Rating |
|---|---|---|
| text.on-accent (graphite.900) `#1E1E1E` on bg.accent `#7DFFFF` | 13.99:1 | AAA |
| graphite.900 text `#1E1E1E` on accent-hover fill `#B3FFFF` | 14.82:1 | AAA |
| graphite.900 text `#1E1E1E` on accent-pressed fill `#4FE0E6` | 10.43:1 | AAA |
| graphite.900 text `#1E1E1E` on dusk.300 fill `#F0A98A` | 8.53:1 | AAA |
| mono logo ink `#1E1E1E` on white (light contexts) `#FFFFFF` | 16.67:1 | AAA |
| accent `#7DFFFF` on white (NOT allowed) `#FFFFFF` | 1.19:1 | fail, never use |
| accent `#7DFFFF` on stone.100 (NOT allowed) `#F2EFE9` | 1.04:1 | fail, never use |
