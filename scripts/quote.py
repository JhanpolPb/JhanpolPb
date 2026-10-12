"""Genera la sección Quote como pantalla de carga de videojuego (assets/quote.svg)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pixel import text, width, ctext, stepped

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "quote.svg")
QUOTES = [
    "CODE. LEARN. BUILD. REPEAT.",
    "EVERY BUG IS JUST ANOTHER BOSS FIGHT.",
    "SHIP IT, LEARN FROM IT, LEVEL UP.",
]
W, H, PX = 820, 150, 3
STEP = 4  # segundos por cita
DUR = STEP * len(QUOTES)


def show_only(i):
    """Animación discreta: el grupo i es visible solo durante su turno."""
    n = len(QUOTES)
    values = ";".join("1" if k == i else "0" for k in range(n))
    times = ";".join(f"{k / n:.4f}" for k in range(n))
    return (f'<animate attributeName="opacity" values="{values}" keyTimes="{times}" '
            f'dur="{DUR}s" repeatCount="indefinite" calcMode="discrete"/>')


o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" shape-rendering="crispEdges">']

# cita que rota, precedida de "TIP:"
for i, q in enumerate(QUOTES):
    line = "TIP: " + q
    x = (W - width(line, PX)) / 2
    tip_w = width("TIP: ", PX) + PX
    o.append(f'<g opacity="{1 if i == 0 else 0}">'
             f'{text("TIP:", x + PX / 2 * 1, 22, PX, "#5c0a0a")}{text("TIP:", x, 20, PX, "#fbd000")}'
             f'{text(q, x + tip_w + 1.5, 22, PX, "#5c0a0a")}{text(q, x + tip_w, 20, PX, "#ffffff")}'
             f'{show_only(i)}</g>')

# barra de carga que se llena en cada cita
segs, bx, by, sw = 30, 160, 66, 16
bw = segs * (sw + 4) + 8
o.append(stepped(bx - 6, by - 6, bw + 4, 36, 4, "#ffffff"))
o.append(stepped(bx - 2, by - 2, bw - 4, 28, 3, "#0d1117"))
for k in range(segs):
    t = (k + 1) / (segs + 2)
    x = bx + 2 + k * (sw + 4)
    o.append(f'<g opacity="0"><rect x="{x}" y="{by + 2}" width="{sw}" height="16" fill="#e52521"/>'
             f'<rect x="{x}" y="{by + 2}" width="{sw}" height="4" fill="#ff7b72"/>'
             f'<animate attributeName="opacity" values="0;1" keyTimes="0;{t:.4f}" dur="{STEP}s" '
             f'repeatCount="indefinite" calcMode="discrete"/></g>')

# "NOW LOADING" parpadeando
o.append(f'<g>{ctext("NOW LOADING...", W / 2, 118, 2, "#8b949e")}'
         '<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.2s" '
         'repeatCount="indefinite" calcMode="discrete"/></g>')
o.append('</svg>')

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(o))
