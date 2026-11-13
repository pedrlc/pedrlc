#!/usr/bin/env python3
"""Gera os SVGs animados do README do perfil (tema painel de carro / OBD2).

Uso:  python3 profile/gen_assets.py
Gera os SVGs na mesma pasta do script (tudo em profile/, sem subpastas).
Edite os textos e cores nas constantes abaixo e rode de novo para regenerar.
"""
import math
import os
import sys

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
A = OUT
os.makedirs(A, exist_ok=True)

# ---------- paleta ----------
BG, PANEL, LINE = "#0b0f14", "#111821", "#1f2a37"
CY, AM, GR, RD = "#22d3ee", "#f59e0b", "#34d399", "#ef4444"
TX, MU = "#e5e7eb", "#6b7280"
MONO = "'JetBrains Mono','Cascadia Code',Consolas,'SF Mono',Menlo,monospace"
SANS = "'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif"


def save(path, content):
    with open(os.path.join(A, path), "w", encoding="utf-8") as f:
        f.write(content)


def pt(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def arc(cx, cy, r, a0, a1):
    x0, y0 = pt(cx, cy, r, a0)
    x1, y1 = pt(cx, cy, r, a1)
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return f"M{x0:.1f} {y0:.1f} A{r} {r} 0 {large} 1 {x1:.1f} {y1:.1f}"


def brackets(w, h, color=LINE, s=14, m=8):
    return (
        f'<path d="M{m} {m+s} V{m} H{m+s} M{w-m-s} {m} H{w-m} V{m+s} '
        f'M{m} {h-m-s} V{h-m} H{m+s} M{w-m-s} {h-m} H{w-m} V{h-m-s}" '
        f'fill="none" stroke="{color}" stroke-width="1.5"/>'
    )


# =====================================================================
# HEADER 1200x320
# =====================================================================
def header():
    W, H = 1200, 320
    cx, cy, R = 985, 158, 112
    s = []
    s.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img">')
    s.append("<title>Pedro Lucas - Engenharia de Software, Mobile e Full Stack</title>")
    s.append(f"""<defs>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0H0V40" fill="none" stroke="{CY}" stroke-opacity=".06"/>
  </pattern>
  <radialGradient id="glow" cx="{cx/W:.3f}" cy="{cy/H:.3f}" r=".42">
    <stop offset="0" stop-color="{CY}" stop-opacity=".20"/>
    <stop offset="1" stop-color="{CY}" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="tg" x1="0" x2="1">
    <stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="{CY}"/>
  </linearGradient>
  <filter id="blur"><feGaussianBlur stdDeviation="6"/></filter>
  <clipPath id="rv"><rect x="0" y="0" width="0" height="{H}">
    <animate attributeName="width" from="0" to="820" dur="1.4s" begin="0.2s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines=".2 .7 .2 1"/>
  </rect></clipPath>
  <style>
    @keyframes blink{{50%{{fill-opacity:0}}}}
    .cur{{animation:blink 1s steps(1) infinite}}
  </style>
</defs>""")
    s.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
    s.append(f'<rect width="{W}" height="{H}" fill="url(#grid)"/>')
    s.append(f'<rect width="{W}" height="{H}" fill="url(#glow)"/>')
    s.append(brackets(W, H, "#2a3948", 18, 12))

    # status
    s.append(f'<g font-family="{MONO}" font-size="12" letter-spacing="2">')
    s.append(f'<circle cx="62" cy="45" r="4" fill="{GR}"><animate attributeName="opacity" values="1;.25;1" dur="1.6s" repeatCount="indefinite"/></circle>')
    s.append(f'<text x="76" y="49" fill="{MU}">OBD://PEDROLC  ·  ONLINE</text>')
    s.append(f'<text x="60" y="282" fill="{MU}">FLUTTER · DART · NODE · TS</text>')
    s.append("</g>")

    # titulo (revelado da esquerda p/ direita)
    s.append('<g clip-path="url(#rv)">')
    s.append(f'<text x="58" y="148" font-family="{SANS}" font-size="84" font-weight="800" fill="url(#tg)" letter-spacing="-1">Pedro Lucas</text>')
    s.append("</g>")
    s.append(f'<rect x="60" y="168" width="150" height="4" rx="2" fill="{AM}"><animate attributeName="width" from="0" to="150" dur="1s" begin="0.9s" fill="freeze"/></rect>')
    s.append(f'<text x="60" y="206" font-family="{MONO}" font-size="15" letter-spacing="4" fill="{CY}">ENGENHARIA DE SOFTWARE  /  MOBILE  /  FULL STACK</text>')
    s.append(
        f'<text x="60" y="250" font-family="{MONO}" font-size="19" fill="{TX}">&gt; diagnosticando carros, escrevendo código'
        f'<tspan class="cur" fill="{AM}">▌</tspan></text>'
    )

    # tacometro
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{R+14}" fill="{PANEL}" stroke="{LINE}" stroke-width="2"/>')
    s.append(f'<path d="{arc(cx,cy,R,135,405)}" fill="none" stroke="{LINE}" stroke-width="10" stroke-linecap="round"/>')
    red0 = 135 + 270 * 6.5 / 8
    s.append(f'<path d="{arc(cx,cy,R,135,red0)}" fill="none" stroke="{CY}" stroke-opacity=".55" stroke-width="10" stroke-linecap="round"/>')
    s.append(f'<path d="{arc(cx,cy,R,red0,405)}" fill="none" stroke="{RD}" stroke-opacity=".85" stroke-width="10" stroke-linecap="round"/>')
    for i in range(9):
        a = 135 + i * 33.75
        x0, y0 = pt(cx, cy, R - 10, a)
        x1, y1 = pt(cx, cy, R - 26, a)
        col = RD if i >= 7 else TX
        s.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{col}" stroke-width="3" stroke-linecap="round"/>')
        tx, ty = pt(cx, cy, R - 44, a)
        s.append(f'<text x="{tx:.1f}" y="{ty:.1f}" dy=".35em" text-anchor="middle" font-family="{MONO}" font-size="14" font-weight="700" fill="{col}">{i}</text>')
    for i in range(8):
        a = 135 + i * 33.75 + 16.875
        x0, y0 = pt(cx, cy, R - 10, a)
        x1, y1 = pt(cx, cy, R - 19, a)
        s.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{MU}" stroke-width="2" stroke-linecap="round"/>')
    s.append(f'<text x="{cx}" y="{cy+58}" text-anchor="middle" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{MU}">RPM x1000</text>')
    s.append(f'<text x="{cx}" y="{cy+78}" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="700" letter-spacing="3" fill="{AM}">VRUM</text>')

    angles = [135, 135, 338, 296, 350, 262, 150, 135]
    times = "0;.10;.28;.38;.52;.66;.84;1"
    vals = ";".join(f"{a} {cx} {cy}" for a in angles)
    splines = ";".join([".4 0 .2 1"] * 7)
    s.append(f'<g><animateTransform attributeName="transform" type="rotate" values="{vals}" keyTimes="{times}" calcMode="spline" keySplines="{splines}" dur="8s" repeatCount="indefinite"/>')
    s.append(f'<line x1="{cx-18}" y1="{cy}" x2="{cx+R-16}" y2="{cy}" stroke="{AM}" stroke-width="4" stroke-linecap="round"/>')
    s.append("</g>")
    s.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="{BG}" stroke="{AM}" stroke-width="3"/>')

    # estrada
    s.append(f'<rect x="0" y="296" width="{W}" height="24" fill="#0e141b"/>')
    s.append(f'<line x1="0" y1="296.5" x2="{W}" y2="296.5" stroke="{LINE}"/>')
    s.append(
        f'<line x1="-44" y1="308" x2="{W+44}" y2="308" stroke="{AM}" stroke-opacity=".7" stroke-width="3" stroke-dasharray="26 18">'
        '<animate attributeName="stroke-dashoffset" from="0" to="-44" dur=".7s" repeatCount="indefinite"/></line>'
    )
    s.append("</svg>")
    save("header.svg", "\n".join(s))


# =====================================================================
# TITULOS DE SECAO 880x44
# =====================================================================
def title(slug, num, label, tag):
    W, H = 880, 44
    x_label = 66
    x_line0 = x_label + len(label) * 14 + 18
    x_line1 = W - 22 - len(tag) * 8 - 14
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img">']
    s.append(f"<title>{num} / {label}</title>")
    s.append(f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="6" fill="#0e141b" stroke="{LINE}"/>')
    s.append(f'<rect x="0" y="7" width="4" height="30" fill="{AM}"/>')
    s.append(f'<text x="18" y="27" font-family="{MONO}" font-size="14" font-weight="700" fill="{AM}">{num}</text>')
    s.append(f'<text x="40" y="27" font-family="{MONO}" font-size="14" fill="{MU}">//</text>')
    s.append(f'<text x="{x_label}" y="29" font-family="{SANS}" font-size="19" font-weight="800" letter-spacing="3" fill="{TX}">{label}</text>')
    s.append(f'<line x1="{x_line0}" y1="22" x2="{x_line1}" y2="22" stroke="{LINE}" stroke-width="2"/>')
    s.append(
        f'<circle cx="{x_line0}" cy="22" r="3" fill="{CY}"><animate attributeName="cx" values="{x_line0};{x_line1};{x_line0}" dur="6s" repeatCount="indefinite"/></circle>'
    )
    s.append(f'<text x="{W-18}" y="26" text-anchor="end" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{MU}">{tag}</text>')
    s.append("</svg>")
    save(f"title-{slug}.svg", "\n".join(s))


# =====================================================================
# CARTAO SOBRE 880x340
# =====================================================================
def about():
    W, H = 880, 360
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img">']
    s.append("<title>Sobre Pedro Lucas</title>")
    s.append(f"""<defs><clipPath id="c"><rect width="{W}" height="{H}" rx="8"/></clipPath>
<linearGradient id="scan" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{CY}" stop-opacity="0"/><stop offset="1" stop-color="{CY}" stop-opacity=".10"/></linearGradient></defs>""")
    s.append(f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="8" fill="{PANEL}" stroke="{LINE}"/>')
    s.append('<g clip-path="url(#c)">')
    s.append(
        f'<rect x="0" y="-60" width="{W}" height="60" fill="url(#scan)"><animateTransform attributeName="transform" type="translate" values="0 0;0 {H+60}" dur="6s" repeatCount="indefinite"/></rect>'
    )
    s.append("</g>")
    s.append(brackets(W, H, "#2a3948"))
    intro = [
        "Estudante de Engenharia de Software e co-fundador &amp; CTO da Vrum.",
        "Construo apps mobiles com Flutter, automações e sistemas,",
        "porque quero entregar produtos completos, do aparelho ao servidor.",
    ]
    for i, line in enumerate(intro):
        s.append(f'<text x="40" y="{54+i*28}" font-family="{SANS}" font-size="18" fill="{TX}">{line}</text>')
    s.append(f'<line x1="40" y1="142" x2="{W-40}" y2="142" stroke="{LINE}"/>')
    s.append(f'<rect x="40" y="140" width="40" height="4" fill="{AM}"/>')
    rows = [
        ("STATUS", "Cursando Engenharia de Software no IDP · Brasília-DF"),
        ("PROJETO", "Vrum: diagnóstico automotivo OBD2 em tempo real, feito em Flutter"),
        ("STACK", ["Flutter · Dart · JavaScript · TypeScript · Node.js · Python", "LLMs · Machine Learning · Deep Learning"]),
        ("EM TREINO", "Back-end com PostgreSQL e Docker"),
        ("ABERTO A", "Colaborações em projetos web, mobile e automações"),
    ]
    y = 180
    for k, v in rows:
        lines = v if isinstance(v, list) else [v]
        s.append(f'<rect x="40" y="{y-5}" width="7" height="7" fill="{AM}" transform="rotate(45 43.5 {y-1.5})"/>')
        s.append(f'<text x="62" y="{y}" font-family="{MONO}" font-size="12" font-weight="700" letter-spacing="2" fill="{AM}">{k}</text>')
        for j, line in enumerate(lines):
            s.append(f'<text x="190" y="{y+1+j*22}" font-family="{SANS}" font-size="16" fill="{TX}">{line}</text>')
        y += 36 + (len(lines) - 1) * 22
    s.append("</svg>")
    save("about-card.svg", "\n".join(s))


# =====================================================================
# CARTAO VRUM 880x250
# =====================================================================
def vrum():
    W, H = 880, 250
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img">']
    s.append("<title>Vrum - scanner OBD2 em Flutter</title>")
    s.append(f"""<defs><linearGradient id="vg" x1="0" x2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="{CY}"/></linearGradient></defs>""")
    s.append(f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="8" fill="{PANEL}" stroke="{LINE}"/>')
    s.append(brackets(W, H, "#2a3948"))
    s.append(f'<text x="40" y="82" font-family="{SANS}" font-size="52" font-weight="800" letter-spacing="2" fill="url(#vg)">VRUM</text>')
    s.append(f'<text x="42" y="108" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{MU}">SCANNER OBD2  ·  FLUTTER  ·  BLE</text>')
    bullets = [
        "Leitura ao vivo: RPM, velocidade, temperatura e bateria",
        "Códigos de falha explicados em linguagem simples",
        "TireScan AI: análise de pneus 100% no aparelho",
    ]
    for i, b in enumerate(bullets):
        y = 150 + i * 30
        s.append(f'<rect x="42" y="{y-9}" width="7" height="7" fill="{AM}" transform="rotate(45 45.5 {y-5.5})"/>')
        s.append(f'<text x="62" y="{y}" font-family="{SANS}" font-size="16" fill="{TX}">{b}</text>')

    # telemetria
    bx, bw = 520, 320
    s.append(f'<circle cx="{bx+4}" cy="42" r="4" fill="{RD}"><animate attributeName="opacity" values="1;.2;1" dur="1.2s" repeatCount="indefinite"/></circle>')
    s.append(f'<text x="{bx+16}" y="46" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{MU}">TELEMETRIA AO VIVO</text>')
    bars = [
        ("RPM", CY, "70;250;110;300;80;220;70", "4.8s"),
        ("TEMP", AM, "170;178;190;200;190;178;170", "9s"),
        ("BATERIA", GR, "262;258;266;260;264;258;262", "6s"),
    ]
    for i, (name, col, vals, dur) in enumerate(bars):
        y = 78 + i * 36
        s.append(f'<text x="{bx}" y="{y}" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{MU}">{name}</text>')
        s.append(f'<rect x="{bx}" y="{y+8}" width="{bw}" height="10" rx="5" fill="{LINE}"/>')
        s.append(
            f'<rect x="{bx}" y="{y+8}" width="100" height="10" rx="5" fill="{col}"><animate attributeName="width" values="{vals}" dur="{dur}" repeatCount="indefinite" calcMode="spline" keyTimes="0;.17;.33;.5;.67;.83;1" keySplines="{";".join([".4 0 .2 1"]*6)}"/></rect>'
        )
    s.append(f'<rect x="{bx}" y="196" width="{bw}" height="34" rx="6" fill="#1a1405" stroke="{AM}" stroke-opacity=".6"/>')
    s.append(f'<circle cx="{bx+18}" cy="213" r="5" fill="{AM}"><animate attributeName="opacity" values="1;.3;1" dur="1.4s" repeatCount="indefinite"/></circle>')
    s.append(f'<text x="{bx+34}" y="217" font-family="{MONO}" font-size="12" fill="{AM}">P0301  Falha de ignição no cilindro 1</text>')
    s.append(f'<text x="{bx+bw}" y="190" text-anchor="end" font-family="{MONO}" font-size="10" letter-spacing="2" fill="{MU}">EXEMPLO ILUSTRATIVO</text>')
    s.append("</svg>")
    save("vrum-card.svg", "\n".join(s))


# =====================================================================
# DIVISOR 880x20 e RODAPE 1200x150
# =====================================================================
def divider():
    W, H = 880, 20
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" aria-hidden="true">']
    s.append(f'<line x1="0" y1="10" x2="{W/2-16}" y2="10" stroke="{LINE}" stroke-width="2"/>')
    s.append(f'<line x1="{W/2+16}" y1="10" x2="{W}" y2="10" stroke="{LINE}" stroke-width="2"/>')
    s.append(f'<rect x="{W/2-5}" y="5" width="10" height="10" fill="{AM}" transform="rotate(45 {W/2} 10)"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></rect>')
    s.append("</svg>")
    save("divider.svg", "\n".join(s))


def footer():
    W, H = 1200, 150
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img">']
    s.append("<title>Vrum. Seguindo em frente.</title>")
    s.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
    s.append(f'<text x="{W/2}" y="52" text-anchor="middle" font-family="{SANS}" font-size="30" font-weight="800" fill="{TX}">Vrum. Seguindo em frente.</text>')
    s.append(f'<text x="{W/2}" y="78" text-anchor="middle" font-family="{MONO}" font-size="13" letter-spacing="3" fill="{MU}">OBRIGADO POR PASSAR POR AQUI</text>')
    s.append(f'<rect x="0" y="118" width="{W}" height="32" fill="#0e141b"/>')
    s.append(f'<line x1="0" y1="118.5" x2="{W}" y2="118.5" stroke="{LINE}"/>')
    s.append(
        f'<line x1="-44" y1="136" x2="{W+44}" y2="136" stroke="{AM}" stroke-opacity=".6" stroke-width="3" stroke-dasharray="26 18"><animate attributeName="stroke-dashoffset" from="0" to="-44" dur=".7s" repeatCount="indefinite"/></line>'
    )

    def wheel(x):
        return (
            f'<g transform="translate({x} 38)"><circle r="11" fill="#05080b" stroke="{MU}" stroke-width="2"/>'
            f'<g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur=".5s" repeatCount="indefinite"/>'
            f'<line x1="-8" y1="0" x2="8" y2="0" stroke="{MU}" stroke-width="2"/><line x1="0" y1="-8" x2="0" y2="8" stroke="{MU}" stroke-width="2"/></g></g>'
        )

    car = (
        f'<g><animateTransform attributeName="transform" type="translate" values="-180 80;{W+60} 80" dur="9s" repeatCount="indefinite"/>'
        f'<path d="M0 36 Q0 14 20 12 L38 -6 Q42 -10 50 -10 H92 Q100 -10 106 -4 L122 12 Q146 14 146 36 Z" fill="{CY}"/>'
        f'<path d="M44 -2 H64 V12 H34 Z M70 -2 H92 L108 12 H70 Z" fill="{BG}" opacity=".85"/>'
        f'<rect x="138" y="20" width="8" height="6" rx="2" fill="{AM}"/>'
        f'{wheel(32)}{wheel(112)}</g>'
    )
    s.append(car)
    s.append("</svg>")
    save("footer.svg", "\n".join(s))


if __name__ == "__main__":
    header()
    title("about", "01", "SOBRE", "PID 0x01")
    title("vrum", "02", "PROJETO", "PID 0x02")
    title("skills", "03", "ARSENAL", "PID 0x03")
    title("stats", "04", "STATUS", "PID 0x04")
    title("arcade", "05", "ARCADE", "PID 0x05")
    title("contact", "06", "CONTATO", "PID 0x06")
    about()
    vrum()
    divider()
    footer()
    print("ok ->", A)
