import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pixel import text, width, ctext, stepped, coin, spark


def build(score, coins):
    W,H=820,230
    name="JHANPOL PARRA BARRETO"
    bx,by,bw,bh,s=110,62,600,112,8
    o=6
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" shape-rendering="crispEdges">']
    # HUD
    svg.append(text(f"SCORE {score:06d}",30,14,3,"#fbd000"))
    svg.append(coin(W/2-40,24,3,0))
    svg.append(text(f"X {coins}",W/2-22,14,3,"#fbd000"))
    svg.append(text("WORLD 1-1",W-30-width("WORLD 1-1",3),14,3,"#fbd000"))
    # shadow / 3D base
    svg.append(stepped(bx-o,by-o+12,bw+2*o,bh+2*o,s,"#1a0505"))
    svg.append(stepped(bx,by+12,bw,bh,s,"#7a0c0c"))
    # button (pressable)
    btn=[stepped(bx-o,by-o,bw+2*o,bh+2*o,s,"#1a0505"),
         stepped(bx,by,bw,bh,s,"#e52521"),
         f'<rect x="{bx+s}" y="{by+bh-3*s}" width="{bw-2*s}" height="{s}" fill="#c41a17"/>',
         f'<rect x="{bx+2*s}" y="{by+bh-2*s}" width="{bw-4*s}" height="{s}" fill="#a31512"/>',
         f'<rect x="{bx+2*s}" y="{by+s}" width="{bw-6*s}" height="{s/2*1}" fill="#ff7b72"/>',
         f'<rect x="{bx+s}" y="{by+2*s}" width="{s/2}" height="{s*2}" fill="#ff7b72"/>',
         ctext(name,W/2,by+22,4,"#ffffff","#5c0a0a"),
         f'<g>{ctext("> PRESS START",W/2,by+70,3,"#fbd000","#5c0a0a")}<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.1s" repeatCount="indefinite" calcMode="discrete"/></g>']
    svg.append('<g>'+''.join(btn)+'<animateTransform attributeName="transform" type="translate" values="0 0;0 0;0 9;0 9;0 0" keyTimes="0;0.82;0.86;0.92;1" dur="3.5s" repeatCount="indefinite"/></g>')
    # coins & sparkles
    svg.append(coin(55,118,5,0.3)); svg.append(coin(W-55,118,5,0.9))
    for x,y,d in [(95,50,0),(730,52,0.7),(80,190,1.3),(745,195,0.4),(400,215,1.0)]:
        svg.append(spark(x,y,3,d))
    svg.append('</svg>')
    return '\n'.join(svg)
