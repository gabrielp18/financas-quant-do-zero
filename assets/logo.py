"""Gera o logo do repositório: um zero cortado por um passeio aleatório de verdade.

  python assets/logo.py  ->  assets/logo.svg

O rabisco é o mesmo passeio do vídeo "O passeio aleatório": default_rng(52), 1.000 lançamentos de moeda,
preço começando em 100. Ele cai até 86, sobe até 131 e termina em 128; o ponto dourado é onde ele termina.
"""
from pathlib import Path

import numpy as np

NAVY, PAPER, BLUE, GOLD = "#1B2A4A", "#F5F6FA", "#5B8DEF", "#F2B544"

rng = np.random.default_rng(52)
step = np.where(rng.random(1000) < 0.5, 1, -1)
price = 100 + np.concatenate([[0], step.cumsum()])
assert (price.min(), price.max(), price[-1]) == (86, 131, 128)

idx = np.unique(np.r_[np.arange(0, len(price), 8), len(price) - 1])
x = 34 + (idx / idx[-1]) * 180                       # de 34 a 214: passa das bordas do zero, como a barra de um Ø
y = 182 - (price[idx] - 86) / (131 - 86) * 108       # de 182 (o fundo, 86) a 74 (o topo, 131)
pts = " ".join(f"{a:.1f},{b:.1f}" for a, b in zip(x, y))
grade = "".join(f'<path d="M{k} 0V256M0 {k}H256"/>' for k in range(32, 256, 32))

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" role="img" aria-label="Finanças Quantitativas do Zero">
  <defs><clipPath id="c"><rect width="256" height="256" rx="56"/></clipPath></defs>
  <rect width="256" height="256" rx="56" fill="{NAVY}"/>
  <g clip-path="url(#c)" stroke="#FFFFFF" stroke-opacity=".07" stroke-width="1.5">{grade}</g>
  <ellipse cx="128" cy="128" rx="60" ry="84" fill="none" stroke="{PAPER}" stroke-width="18"/>
  <g fill="none" stroke-linecap="round" stroke-linejoin="round">
    <polyline points="{pts}" stroke="{NAVY}" stroke-width="18"/>
    <polyline points="{pts}" stroke="{BLUE}" stroke-width="6.5"/>
  </g>
  <circle cx="{x[0]:.1f}" cy="{y[0]:.1f}" r="7" fill="{BLUE}"/>
  <circle cx="{x[-1]:.1f}" cy="{y[-1]:.1f}" r="12" fill="{GOLD}" stroke="{NAVY}" stroke-width="5"/>
</svg>
"""
out = Path(__file__).with_name("logo.svg")
out.write_text(svg, encoding="utf-8")
print(f"{out} · {len(idx)} pontos · fim em ({x[-1]:.0f}, {y[-1]:.0f})")
