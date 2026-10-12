"""Genera los títulos de sección estilo menú de videojuego (assets/titles/*.svg)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pixel import text, width, stepped

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "titles")
PX = 5


def title(label):
    tw = width(label, PX)
    w, h = tw + 120, 82
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" shape-rendering="crispEdges">',
         stepped(0, 6, w, 70, 8, "#1a0505"),            # contorno
         stepped(5, 15, w - 10, 58, 7, "#7a0c0c"),       # relieve inferior
         stepped(5, 9, w - 10, 56, 7, "#e52521"),        # cara del botón
         f'<rect x="19" y="16" width="{w - 50}" height="4" fill="#ff7b72"/>',
         f'<rect x="12" y="23" width="4" height="12" fill="#ff7b72"/>',
         f'<rect x="12" y="{9 + 56 - 10}" width="{w - 24}" height="4" fill="#c41a17"/>',
         # flecha de selección que parpadea
         f'<g>{text(">", 26, 20, PX, "#fbd000")}'
         '<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1s" repeatCount="indefinite" calcMode="discrete"/></g>',
         text(label, 72, 23, PX, "#5c0a0a"),
         text(label, 70, 20, PX, "#ffffff"),
         '</svg>']
    return '\n'.join(o)


os.makedirs(OUT, exist_ok=True)
for slug, label in [("about", "ABOUT ME"), ("stack", "TECH STACK"), ("architecture", "ARCHITECTURE & PATTERNS"),
                    ("contributions", "CONTRIBUTIONS"), ("connect", "CONNECT WITH ME"), ("quote", "QUOTE")]:
    with open(os.path.join(OUT, f"{slug}.svg"), "w", encoding="utf-8", newline="\n") as f:
        f.write(title(label))
