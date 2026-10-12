"""Genera los títulos de sección estilo menú de videojuego (assets/titles/*.svg)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pixel import text, width, stepped

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "titles")
PX = 4


def title(label):
    tw = width(label, PX)
    w, h = tw + 96, 66
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" shape-rendering="crispEdges">',
         stepped(0, 5, w, 56, 6, "#1a0505"),            # contorno
         stepped(4, 12, w - 8, 46, 6, "#7a0c0c"),        # relieve inferior
         stepped(4, 7, w - 8, 45, 6, "#e52521"),         # cara del botón
         f'<rect x="16" y="13" width="{w - 40}" height="3" fill="#ff7b72"/>',
         f'<rect x="10" y="19" width="3" height="10" fill="#ff7b72"/>',
         f'<rect x="10" y="{7 + 45 - 8}" width="{w - 20}" height="3" fill="#c41a17"/>',
         # flecha de selección que parpadea
         f'<g>{text(">", 22, 16, PX, "#fbd000")}'
         '<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1s" repeatCount="indefinite" calcMode="discrete"/></g>',
         text(label, 58, 18, PX, "#5c0a0a"),
         text(label, 56, 16, PX, "#ffffff"),
         '</svg>']
    return '\n'.join(o)


os.makedirs(OUT, exist_ok=True)
for slug, label in [("about", "ABOUT ME"), ("stack", "TECH STACK"), ("architecture", "ARCHITECTURE & PATTERNS"),
                    ("contributions", "CONTRIBUTIONS"), ("connect", "CONNECT WITH ME"), ("quote", "QUOTE")]:
    with open(os.path.join(OUT, f"{slug}.svg"), "w", encoding="utf-8", newline="\n") as f:
        f.write(title(label))
