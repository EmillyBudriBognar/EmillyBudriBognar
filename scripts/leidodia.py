#!/usr/bin/env python3
"""Gera assets/leidodia.svg - a Lei de UX do Dia.

Toda madrugada o painel troca de lei: nome, explicacao em uma frase e um
diagrama desenhado a mao que mostra a ideia funcionando. A escolha vem da
data (semente deterministica), entao o mesmo dia mostra sempre a mesma lei
em qualquer maquina. Sem API, sem dependencia externa.
"""

from datetime import datetime, timedelta, timezone

import temas

BR_TZ = timezone(timedelta(hours=-3))

ROXO, AZUL, ROSA, TINTA, SUAVE, LINHA = "#7e22ce", "#2563eb", "#db2777", "#111827", "#4b5563", "#e9d5ff"


def pilula(x, y, w, h, cor=LINHA, fill="none", op=1):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2}" fill="{fill}" '
            f'stroke="{cor}" stroke-width="1.6" opacity="{op}"/>')


# ── os diagramas ─────────────────────────────────────────────────────────
# cada um vive numa caixa de 360x166, com a origem no canto superior esquerdo

FITTS = f"""
  <g stroke-dasharray="4 5" stroke-width="1.4" fill="none" opacity=".55">
    <path d="M40 136 L108 76" stroke="{ROXO}"/>
    <path d="M40 136 L278 58" stroke="{SUAVE}"/>
  </g>
  <circle cx="120" cy="64" r="30" fill="{ROXO}" fill-opacity=".16" stroke="{ROXO}" stroke-width="2"/>
  <circle class="pulso" cx="120" cy="64" r="30" fill="none" stroke="{ROXO}" stroke-width="2"/>
  <path d="M111 64 l6 6.5 12 -13" fill="none" stroke="{ROXO}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="288" cy="54" r="9" fill="{SUAVE}" fill-opacity=".16" stroke="{SUAVE}" stroke-width="1.8"/>
  <g class="seta"><path d="M32 128 l0 22 5.5 -6.5 5.5 12 5 -2.4 -5.5 -12 7.5 0 z" fill="{TINTA}"/></g>
  <text x="120" y="118" font-size="9.5" letter-spacing="1.4" text-anchor="middle" fill="{ROXO}">PERTO E GRANDE</text>
  <text x="288" y="80" font-size="9.5" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">LONGE E PEQUENO</text>
"""

HICK = f"""
  {''.join(pilula(24, 34 + i * 28, 116, 18, ROXO, ROXO + '22') for i in range(3))}
  {''.join(pilula(214, 22 + i * 19, 116, 13, SUAVE, 'none', .8) for i in range(6))}
  <rect class="barra" x="24" y="140" width="44" height="7" rx="3.5" fill="{ROXO}"/>
  <rect class="barra b2" x="214" y="140" width="116" height="7" rx="3.5" fill="{ROSA}"/>
  <text x="82" y="164" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{ROXO}">DECIDE RÁPIDO</text>
  <text x="272" y="164" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{ROSA}">TRAVA</text>
"""


def _tela(x, destaque=False):
    cor = ROXO if destaque else SUAVE
    op = "1" if destaque else ".55"
    return f"""
  <g opacity="{op}">
    <rect x="{x}" y="26" width="92" height="114" rx="12" fill="none" stroke="{cor}" stroke-width="1.8"/>
    <rect x="{x + 12}" y="40" width="68" height="9" rx="4.5" fill="{cor}"/>
    <rect x="{x + 12}" y="58" width="46" height="6" rx="3" fill="{cor}" opacity=".5"/>
    <rect x="{x + 12}" y="70" width="56" height="6" rx="3" fill="{cor}" opacity=".5"/>
    <rect x="{x + 12}" y="88" width="68" height="34" rx="8" fill="{cor}" opacity=".18"/>
  </g>"""


JAKOB = f"""
  {_tela(24)}{_tela(134)}{_tela(244, True)}
  <text x="290" y="158" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{ROXO}">O SEU</text>
"""

MILLER = f"""
  {''.join(f'<rect x="{24 + i * 44}" y="30" width="30" height="30" rx="8" fill="{SUAVE}" fill-opacity=".18" stroke="{SUAVE}" stroke-width="1.5"/>' for i in range(7))}
  <text x="180" y="80" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">SETE SOLTOS</text>
  <g>
    {''.join(f'<rect x="{28 + i * 34}" y="104" width="26" height="26" rx="7" fill="{ROXO}" fill-opacity=".18" stroke="{ROXO}" stroke-width="1.5"/>' for i in range(2))}
    {''.join(f'<rect x="{136 + i * 34}" y="104" width="26" height="26" rx="7" fill="{ROXO}" fill-opacity=".18" stroke="{ROXO}" stroke-width="1.5"/>' for i in range(3))}
    {''.join(f'<rect x="{278 + i * 34}" y="104" width="26" height="26" rx="7" fill="{ROXO}" fill-opacity=".18" stroke="{ROXO}" stroke-width="1.5"/>' for i in range(2))}
    <g stroke="{ROXO}" stroke-width="1.6" fill="none" opacity=".6">
      <path d="M24 138 v6 h64 v-6"/><path d="M132 138 v6 h98 v-6"/><path d="M274 138 v6 h64 v-6"/>
    </g>
  </g>
  <text x="180" y="162" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{ROXO}">TRÊS GRUPOS</text>
"""

VON_RESTORFF = f"""
  {''.join(f'<rect x="{28 + (i % 3) * 108}" y="{38 + (i // 3) * 56}" width="88" height="40" rx="12" fill="{SUAVE}" fill-opacity=".14" stroke="{SUAVE}" stroke-width="1.5" opacity=".7"/>' for i in range(6) if i != 4)}
  <g class="destaca" style="transform-origin:180px 114px">
    <rect x="136" y="94" width="88" height="40" rx="12" fill="{ROSA}" fill-opacity=".2" stroke="{ROSA}" stroke-width="2.4"/>
  </g>
  <circle class="pulso" cx="180" cy="114" r="30" fill="none" stroke="{ROSA}" stroke-width="1.6"/>
"""

ZEIGARNIK = f"""
  <rect x="28" y="60" width="304" height="16" rx="8" fill="{SUAVE}" fill-opacity=".18"/>
  <rect class="enche" x="28" y="60" width="188" height="16" rx="8" fill="{ROXO}"/>
  <text x="332" y="46" font-size="10" letter-spacing="1.2" text-anchor="end" fill="{ROXO}">62%</text>
  <g>
    {''.join(f'<circle cx="{52 + i * 64}" cy="118" r="13" fill="{ROXO}" fill-opacity=".18" stroke="{ROXO}" stroke-width="1.8"/>'
             f'<path d="M{45 + i * 64} 118 l5 5.4 9.5 -10.4" fill="none" stroke="{ROXO}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>' for i in range(3))}
    {''.join(f'<circle cx="{244 + i * 64}" cy="118" r="13" fill="none" stroke="{SUAVE}" stroke-width="1.8" stroke-dasharray="4 4"/>' for i in range(2))}
    <path d="M65 118 H231 M257 118 H295" stroke="{SUAVE}" stroke-width="1.4" opacity=".5"/>
  </g>
  <text x="180" y="152" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">FALTAM DOIS - E ISSO INCOMODA</text>
"""

PICO_FIM = f"""
  <path d="M28 130 L332 130" stroke="{SUAVE}" stroke-width="1.2" opacity=".5"/>
  <path class="curva" d="M28 112 C70 108, 84 44, 124 42 C164 40, 172 104, 214 108 C252 112, 268 96, 300 62"
        fill="none" stroke="{ROXO}" stroke-width="2.6" stroke-linecap="round"/>
  <g stroke-dasharray="4 4" stroke="{ROSA}" stroke-width="1.4" opacity=".7">
    <path d="M124 42 V130"/><path d="M300 62 V130"/>
  </g>
  <circle cx="124" cy="42" r="6" fill="{ROSA}"/>
  <circle class="pulso" cx="124" cy="42" r="6" fill="none" stroke="{ROSA}" stroke-width="1.8"/>
  <circle cx="300" cy="62" r="6" fill="{ROSA}"/>
  <text x="124" y="30" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{ROSA}">PICO</text>
  <text x="300" y="50" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{ROSA}">FIM</text>
  <text x="200" y="152" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">O MEIO QUASE NÃO CONTA</text>
"""

PROXIMIDADE = f"""
  <g fill="{ROXO}">
    {''.join(f'<circle cx="{52 + (i % 3) * 26}" cy="{56 + (i // 3) * 26}" r="7"/>' for i in range(9))}
  </g>
  <circle cx="78" cy="82" r="52" fill="none" stroke="{ROXO}" stroke-width="1.6" stroke-dasharray="5 5" opacity=".6"/>
  <g fill="{AZUL}">
    {''.join(f'<circle cx="{246 + (i % 3) * 26}" cy="{56 + (i // 3) * 26}" r="7"/>' for i in range(9))}
  </g>
  <circle cx="272" cy="82" r="52" fill="none" stroke="{AZUL}" stroke-width="1.6" stroke-dasharray="5 5" opacity=".6"/>
  <text x="180" y="88" font-size="22" font-weight="700" text-anchor="middle" fill="{SUAVE}" opacity=".45">|</text>
  <text x="180" y="156" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">DOIS GRUPOS, SEM PRECISAR DE TÍTULO</text>
"""

LEIS = [
    ("LEI DE FITTS",
     ["Quanto maior e mais perto o alvo, mais rápido a mão chega nele.",
      "Botão importante não merece ser pequeno nem ficar escondido",
      "num canto que ninguém alcança."], FITTS),
    ("LEI DE HICK",
     ["Cada opção a mais na tela é um segundo a mais de decisão.",
      "Menu enxuto não é menu pobre: é menu que respeita o tempo",
      "de quem está do outro lado."], HICK),
    ("LEI DE JAKOB",
     ["As pessoas passam a maior parte do tempo em outros sites.",
      "Elas esperam que o seu funcione igual. Originalidade fica",
      "na identidade visual, não no lugar do carrinho."], JAKOB),
    ("LEI DE MILLER",
     ["A memória de trabalho segura mais ou menos sete coisas.",
      "Agrupar é o truque: três blocos de dois cansam menos",
      "que sete itens soltos na mesma lista."], MILLER),
    ("EFEITO VON RESTORFF",
     ["O item diferente do resto é o único que fica na memória.",
      "Se tudo está em destaque, nada está. Escolha um botão",
      "para gritar e deixe os outros sussurrarem."], VON_RESTORFF),
    ("EFEITO ZEIGARNIK",
     ["Tarefa começada incomoda até terminar.",
      "Mostrar o progresso não é enfeite: é o que faz a pessoa",
      "voltar para fechar o que ficou pela metade."], ZEIGARNIK),
    ("REGRA DO PICO-FIM",
     ["A lembrança de uma experiência não é a média dela.",
      "É o momento mais intenso somado ao final. Capriche na",
      "confirmação do pedido, e não só no formulário."], PICO_FIM),
    ("LEI DA PROXIMIDADE",
     ["O que está perto parece do mesmo grupo, mesmo sem título.",
      "Antes de desenhar mais uma linha divisória, tente",
      "só mexer no espaçamento."], PROXIMIDADE),
]


def semente(data):
    """Hash estavel a partir de AAAAMMDD - o mesmo dia, a mesma lei."""
    n = int(data.strftime("%Y%m%d"))
    n = (n * 1103515245 + 12345) & 0x7FFFFFFF
    n ^= n >> 13
    return (n * 2654435761) & 0x7FFFFFFF


def montar(agora):
    nome, frases, diagrama = LEIS[semente(agora) % len(LEIS)]
    linhas = "".join(
        f'<text x="40" y="{146 + i * 21}" font-size="12.5" fill="{SUAVE}">{t}</text>'
        for i, t in enumerate(frases))
    data_br = agora.strftime("%d.%m.%Y")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 248" width="1000" height="248" role="img" aria-label="Lei de UX do dia {data_br}: {nome}. {' '.join(frases)}">
  <defs>
    <linearGradient id="lFundo" x1="0" y1="0" x2="0.8" y2="1">
      <stop offset="0%" stop-color="#fffdff"/><stop offset="55%" stop-color="#faf5ff"/><stop offset="100%" stop-color="#f3e8ff"/>
    </linearGradient>
    <radialGradient id="lB1" cx="50%" cy="50%"><stop offset="0%" stop-color="#b06cf0" stop-opacity=".16"/><stop offset="100%" stop-color="#b06cf0" stop-opacity="0"/></radialGradient>
    <linearGradient id="lRegua" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#9333ea"/><stop offset="100%" stop-color="#2563eb"/>
    </linearGradient>
    <clipPath id="lCard"><rect width="1000" height="248" rx="28"/></clipPath>
    <clipPath id="lQuadro"><rect x="600" y="32" width="360" height="166" rx="20"/></clipPath>
    <style>
      .sobe{{animation:sobe .9s cubic-bezier(.2,.7,.3,1) both}}
      .s2{{animation-delay:.1s}}.s3{{animation-delay:.2s}}.s4{{animation-delay:.3s}}
      @keyframes sobe{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:translateY(0)}}}}
      .vivo{{animation:vivo 2.4s ease-in-out infinite}}
      @keyframes vivo{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
      .pulso{{animation:pulso 3s ease-in-out infinite}}
      @keyframes pulso{{0%{{opacity:.7}}70%,100%{{opacity:0}}}}
      .seta{{animation:seta 4s ease-in-out infinite}}
      @keyframes seta{{0%,100%{{transform:translate(0,0)}}45%,55%{{transform:translate(74px,-64px)}}}}
      .barra{{transform-origin:24px 0;animation:cresce 1.2s cubic-bezier(.2,.7,.3,1) .4s both}}
      .b2{{transform-origin:214px 0;animation-delay:.55s}}
      .enche{{transform-origin:28px 0;animation:cresce 1.4s cubic-bezier(.2,.7,.3,1) .4s both}}
      @keyframes cresce{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
      .curva{{stroke-dasharray:420;stroke-dashoffset:420;animation:curva 2s ease-out .4s forwards}}
      @keyframes curva{{to{{stroke-dashoffset:0}}}}
      .destaca{{animation:destaca 3.4s ease-in-out infinite}}
      @keyframes destaca{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.06)}}}}
      @media (prefers-reduced-motion: reduce){{
        *{{animation:none !important}}
        .curva{{stroke-dashoffset:0}} .pulso{{opacity:.4}}
      }}
    </style>
  </defs>

  <g clip-path="url(#lCard)">
    <rect width="1000" height="248" fill="url(#lFundo)"/>
    <ellipse cx="60" cy="230" rx="300" ry="160" fill="url(#lB1)"/>

    <g font-family="Jost, Century Gothic, Futura, Segoe UI, Arial, sans-serif">
      <g class="sobe">
        <circle class="vivo" cx="45" cy="44" r="4.5" fill="#16a34a"/>
        <text x="59" y="48" font-size="10.5" letter-spacing="3" fill="{ROXO}">LEI DE UX DO DIA &#183; {data_br}</text>
      </g>
      <text class="sobe s2" x="38" y="104" font-size="30" font-weight="700" letter-spacing="1.2" fill="{TINTA}">{nome}</text>
      <rect class="sobe s3" x="40" y="118" width="80" height="4" rx="2" fill="url(#lRegua)"/>
      <g class="sobe s3">{linhas}</g>
      <text class="sobe s4" x="40" y="216" font-size="9" letter-spacing="1.4" fill="#6b7280" font-family="SFMono-Regular, Consolas, Menlo, monospace">ATUALIZADA AUTOMATICAMENTE TODA MADRUGADA &#183; UMA LEI DIFERENTE POR DIA</text>

      <g class="sobe s4">
        <rect x="600" y="32" width="360" height="166" rx="20" fill="#fffdff" stroke="{LINHA}" stroke-width="1.6"/>
        <g clip-path="url(#lQuadro)"><g transform="translate(600,32)">{diagrama}</g></g>
      </g>
    </g>

    <rect x="1" y="1" width="998" height="246" rx="28" fill="none" stroke="#9333ea" stroke-opacity=".2" stroke-width="2"/>
  </g>
</svg>
"""


if __name__ == "__main__":
    temas.gravar("leidodia", montar(datetime.now(BR_TZ)))
    print("lei do dia gerada nos dois temas")
