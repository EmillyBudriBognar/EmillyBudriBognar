#!/usr/bin/env python3
"""Gera assets/leidodia.svg - a Lei de UX do Dia.

Toda madrugada o painel troca de lei: nome, explicacao em uma frase e um
diagrama desenhado a mao que mostra a ideia funcionando. A escolha e uma
rotacao fixa pela data: nenhuma lei repete antes de todas terem aparecido,
e o ciclo inteiro leva tantos dias quanto o tamanho da lista.
Sem API, sem dependencia externa.
"""

from datetime import datetime, timedelta, timezone

import temas

BR_TZ = timezone(timedelta(hours=-3))

ROXO, AZUL, ROSA, TINTA, SUAVE, LINHA = "#7e22ce", "#2563eb", "#db2777", "#111827", "#4b5563", "#e9d5ff"
VERDE = "#16a34a"


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

TESLER = f"""
  <text x="96" y="32" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">PESSOA</text>
  <text x="264" y="32" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{ROXO}">SISTEMA</text>
  <path d="M180 42 V142" stroke="{SUAVE}" stroke-width="1.4" stroke-dasharray="4 5" opacity=".55"/>
  {''.join(f'<rect x="52" y="{62 + i * 34}" width="88" height="26" rx="9" fill="{SUAVE}" fill-opacity=".16" stroke="{SUAVE}" stroke-width="1.5"/>' for i in range(2))}
  {''.join(f'<rect x="220" y="{52 + i * 34}" width="88" height="26" rx="9" fill="{ROXO}" fill-opacity=".16" stroke="{ROXO}" stroke-width="1.5"/>' for i in range(3))}
  <g class="seta"><path d="M148 100 h22 m-7 -5 l7 5 -7 5" fill="none" stroke="{ROSA}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></g>
  <text x="180" y="162" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">O TRABALHO MUDA DE LADO, NÃO SOME</text>
"""

PRAGNANZ = f"""
  <g fill="none" stroke="{SUAVE}" stroke-width="1.8" opacity=".75">
    <circle cx="74" cy="68" r="26"/><circle cx="104" cy="84" r="26"/><circle cx="98" cy="50" r="20"/>
  </g>
  <g class="seta"><path d="M164 76 h32 m-10 -7 l10 7 -10 7" fill="none" stroke="{ROSA}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></g>
  <circle cx="272" cy="76" r="34" fill="{ROXO}" fill-opacity=".18" stroke="{ROXO}" stroke-width="2.4"/>
  <circle class="pulso" cx="272" cy="76" r="34" fill="none" stroke="{ROXO}" stroke-width="2"/>
  <text x="180" y="150" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">O OLHO PROCURA A FORMA MAIS SIMPLES</text>
"""

SIMILARIDADE = f"""
  {''.join(f'<circle cx="{62 + (i % 6) * 48}" cy="{46 + (i // 6) * 30}" r="9" fill="{ROXO if (i % 6) in (1, 4) else SUAVE}" fill-opacity="{1 if (i % 6) in (1, 4) else .3}"/>' for i in range(24))}
  <text x="180" y="156" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">A COR AGRUPA EM COLUNAS, SEM UMA LINHA SEQUER</text>
"""

REGIAO_COMUM = f"""
  <rect x="30" y="50" width="152" height="64" rx="18" fill="{ROXO}" fill-opacity=".1" stroke="{ROXO}" stroke-width="1.8"/>
  {''.join(f'<circle cx="{60 + i * 44}" cy="82" r="10" fill="{ROXO}"/>' for i in range(3))}
  {''.join(f'<circle cx="{216 + i * 44}" cy="82" r="10" fill="{SUAVE}" fill-opacity=".4"/>' for i in range(3))}
  <text x="180" y="150" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">A MOLDURA CRIA UM GRUPO SOZINHA</text>
"""

DOHERTY = f"""
  <rect x="40" y="50" width="252" height="14" rx="7" fill="{SUAVE}" fill-opacity=".18"/>
  <rect class="enche" x="40" y="50" width="66" height="14" rx="7" fill="{VERDE}"/>
  <circle cx="122" cy="57" r="11" fill="{VERDE}" fill-opacity=".18"/>
  <path d="M116 57 l4.4 4.6 8 -9" fill="none" stroke="{VERDE}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="332" y="61" font-size="10" text-anchor="end" fill="{VERDE}">0,3s</text>
  <rect x="40" y="100" width="252" height="14" rx="7" fill="{SUAVE}" fill-opacity=".18"/>
  <rect class="enche" x="40" y="100" width="214" height="14" rx="7" fill="{ROSA}"/>
  <circle cx="270" cy="107" r="11" fill="{ROSA}" fill-opacity=".18"/>
  <path d="M265 102 l10 10 M275 102 l-10 10" fill="none" stroke="{ROSA}" stroke-width="2.2" stroke-linecap="round"/>
  <text x="332" y="111" font-size="10" text-anchor="end" fill="{ROSA}">2,4s</text>
  <text x="180" y="150" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">PASSOU DE 0,4s, A ATENÇÃO JÁ FOI EMBORA</text>
"""

POSICAO_SERIAL = f"""
  {''.join(f'<rect x="66" y="{34 + i * 18}" width="234" height="12" rx="6" fill="{SUAVE}" fill-opacity=".22"/>' for i in range(1, 6))}
  <rect x="66" y="34" width="234" height="12" rx="6" fill="{ROXO}"/>
  <rect x="66" y="124" width="234" height="12" rx="6" fill="{ROXO}"/>
  <circle class="pulso" cx="48" cy="40" r="6" fill="none" stroke="{ROXO}" stroke-width="1.8"/>
  <circle cx="48" cy="40" r="4.5" fill="{ROXO}"/>
  <circle cx="48" cy="130" r="4.5" fill="{ROXO}"/>
  <text x="180" y="160" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">O COMEÇO E O FIM SÃO O QUE FICA</text>
"""

ESTETICA = f"""
  <g opacity=".5">
    <rect x="34" y="32" width="130" height="96" rx="10" fill="none" stroke="{SUAVE}" stroke-width="1.8"/>
    <rect x="48" y="48" width="70" height="10" rx="3" fill="{SUAVE}"/>
    <rect x="48" y="66" width="102" height="7" rx="3" fill="{SUAVE}" opacity=".6"/>
    <rect x="48" y="80" width="86" height="7" rx="3" fill="{SUAVE}" opacity=".6"/>
    <rect x="48" y="98" width="64" height="18" rx="4" fill="{SUAVE}" opacity=".5"/>
  </g>
  <g>
    <rect x="196" y="32" width="130" height="96" rx="18" fill="{ROXO}" fill-opacity=".08" stroke="{ROXO}" stroke-width="1.8"/>
    <rect x="212" y="48" width="70" height="10" rx="5" fill="{ROXO}"/>
    <rect x="212" y="66" width="102" height="7" rx="3.5" fill="{ROXO}" opacity=".45"/>
    <rect x="212" y="80" width="86" height="7" rx="3.5" fill="{ROXO}" opacity=".45"/>
    <rect x="212" y="98" width="64" height="18" rx="9" fill="{ROXO}"/>
  </g>
  <g class="bate" style="transform-origin:328px 38px">
    <path d="M328 44 c-5.6 -3.8 -8.2 -6.9 -8.2 -10 a4 4 0 0 1 8.2 -1.9 a4 4 0 0 1 8.2 1.9 c0 3.1 -2.6 6.2 -8.2 10 z" fill="{ROSA}"/>
  </g>
  <text x="180" y="152" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">O MESMO FLUXO PARECE MAIS FÁCIL NO BONITO</text>
"""

OCCAM = f"""
  {''.join(f'<rect x="98" y="{34 + i * 22}" width="176" height="14" rx="7" fill="{ROXO}" fill-opacity=".16" stroke="{ROXO}" stroke-width="1.4"/>' for i in range(3))}
  {''.join(f'<rect x="98" y="{100 + i * 22}" width="176" height="14" rx="7" fill="none" stroke="{SUAVE}" stroke-width="1.4" stroke-dasharray="4 4" opacity=".6"/>' for i in range(2))}
  <g stroke="{ROSA}" stroke-width="2" stroke-linecap="round" opacity=".8">
    <path d="M70 100 l16 16 M86 100 l-16 16"/>
    <path d="M70 122 l16 16 M86 122 l-16 16"/>
  </g>
  <text x="180" y="158" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">TIRE ATÉ COMEÇAR A FAZER FALTA</text>
"""

STATUS = f"""
  <rect x="40" y="42" width="196" height="14" rx="7" fill="{SUAVE}" fill-opacity=".18"/>
  <rect class="enche" x="40" y="42" width="90" height="14" rx="7" fill="{ROXO}"/>
  <text x="248" y="53" font-size="10" fill="{ROXO}">46%</text>
  <g transform="translate(302,49)">
    <circle r="14" fill="none" stroke="{SUAVE}" stroke-width="3" opacity=".28"/>
    <path class="curva" d="M0 -14 a14 14 0 0 1 14 14" fill="none" stroke="{ROXO}" stroke-width="3" stroke-linecap="round"/>
  </g>
  <rect x="40" y="88" width="280" height="40" rx="14" fill="{VERDE}" fill-opacity=".12" stroke="{VERDE}" stroke-width="1.5"/>
  <circle cx="68" cy="108" r="11" fill="{VERDE}" fill-opacity=".2"/>
  <path d="M62 108 l4.4 4.6 8 -9" fill="none" stroke="{VERDE}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="90" y="102" width="124" height="9" rx="4.5" fill="{VERDE}" opacity=".5"/>
  <rect x="90" y="116" width="82" height="7" rx="3.5" fill="{VERDE}" opacity=".3"/>
  <text x="180" y="156" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">A PESSOA NUNCA FICA NO ESCURO</text>
"""

PREVENIR = f"""
  <rect x="30" y="44" width="142" height="34" rx="10" fill="none" stroke="{VERDE}" stroke-width="1.8"/>
  <rect x="44" y="56" width="76" height="9" rx="4.5" fill="{VERDE}" opacity=".45"/>
  <circle cx="150" cy="61" r="9" fill="{VERDE}" fill-opacity=".2"/>
  <path d="M145 61 l3.6 3.8 6.6 -7.4" fill="none" stroke="{VERDE}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="30" y="98" font-size="8.5" letter-spacing="1.2" fill="{VERDE}">AVISA ENQUANTO SE DIGITA</text>
  <rect x="196" y="44" width="142" height="34" rx="10" fill="none" stroke="{ROSA}" stroke-width="1.8"/>
  <rect x="210" y="56" width="76" height="9" rx="4.5" fill="{ROSA}" opacity=".45"/>
  <circle cx="316" cy="61" r="9" fill="{ROSA}" fill-opacity=".2"/>
  <path d="M312 57 l8 8 M320 57 l-8 8" fill="none" stroke="{ROSA}" stroke-width="2" stroke-linecap="round"/>
  <text x="196" y="98" font-size="8.5" letter-spacing="1.2" fill="{ROSA}">RECLAMA DEPOIS DE ENVIAR</text>
  <text x="180" y="142" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">ERRO EVITADO VALE MAIS QUE ERRO EXPLICADO</text>
"""

RECONHECER = f"""
  <rect x="32" y="50" width="140" height="34" rx="10" fill="none" stroke="{SUAVE}" stroke-width="1.8" opacity=".65"/>
  <rect class="cur" x="46" y="58" width="6" height="18" fill="{SUAVE}"/>
  <text x="102" y="118" font-size="24" font-weight="700" text-anchor="middle" fill="{SUAVE}" opacity=".4">?</text>
  <rect x="196" y="40" width="142" height="30" rx="10" fill="{ROXO}" fill-opacity=".12" stroke="{ROXO}" stroke-width="1.8"/>
  <path d="M316 51 l6 7 6 -7" fill="none" stroke="{ROXO}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  {''.join(f'<rect x="196" y="{78 + i * 22}" width="142" height="16" rx="6" fill="{ROXO}" fill-opacity="{.2 - i * 0.05}"/>' for i in range(3))}
  <text x="180" y="152" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">MOSTRE AS OPÇÕES EM VEZ DE COBRAR MEMÓRIA</text>
"""

DESFAZER = f"""
  <rect x="60" y="36" width="240" height="34" rx="10" fill="{SUAVE}" fill-opacity=".16"/>
  <rect x="76" y="48" width="120" height="10" rx="5" fill="{SUAVE}" opacity=".5"/>
  <g stroke="{ROSA}" stroke-width="2" stroke-linecap="round">
    <path d="M266 47 l12 12 M278 47 l-12 12"/>
  </g>
  <rect x="60" y="90" width="240" height="42" rx="14" fill="{ROXO}" fill-opacity=".14" stroke="{ROXO}" stroke-width="1.8"/>
  <path d="M98 111 h-14 m6 -6 l-6 6 6 6" fill="none" stroke="{ROXO}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="114" y="115" font-size="11" letter-spacing="1.6" fill="{ROXO}">DESFAZER</text>
  <text x="180" y="158" font-size="9" letter-spacing="1.4" text-anchor="middle" fill="{SUAVE}">TODA AÇÃO PRECISA DE UM CAMINHO DE VOLTA</text>
"""

# A ordem aqui é a ordem em que as leis aparecem, um dia após o outro.
# Alterna lei clássica e heurística de perto para dois dias seguidos nunca
# soarem parecidos.
LEIS = [
    ("LEI DE FITTS",
     ["Quanto maior e mais perto o alvo, mais rápido a mão chega nele.",
      "Botão importante não merece ser pequeno nem ficar escondido",
      "num canto que ninguém alcança."], FITTS),
    ("VISIBILIDADE DO STATUS",
     ["A interface deve dizer o tempo todo o que está acontecendo.",
      "Barra de progresso, spinner e confirmação não são enfeite:",
      "são o que impede a pessoa de achar que travou."], STATUS),
    ("LEI DE HICK",
     ["Cada opção a mais na tela é um segundo a mais de decisão.",
      "Menu enxuto não é menu pobre: é menu que respeita o tempo",
      "de quem está do outro lado."], HICK),
    ("LEI DA PROXIMIDADE",
     ["O que está perto parece do mesmo grupo, mesmo sem título.",
      "Antes de desenhar mais uma linha divisória, tente",
      "só mexer no espaçamento."], PROXIMIDADE),
    ("EFEITO ZEIGARNIK",
     ["Tarefa começada incomoda até terminar.",
      "Mostrar o progresso não é enfeite: é o que faz a pessoa",
      "voltar para fechar o que ficou pela metade."], ZEIGARNIK),
    ("LEI DE TESLER",
     ["Toda complexidade que não dá para eliminar alguém carrega.",
      "A escolha é sua: ou o sistema resolve, ou a conta sobra",
      "para quem está usando."], TESLER),
    ("LEI DE JAKOB",
     ["As pessoas passam a maior parte do tempo em outros sites.",
      "Elas esperam que o seu funcione igual. Originalidade fica",
      "na identidade visual, não no lugar do carrinho."], JAKOB),
    ("LIMIAR DE DOHERTY",
     ["Acima de 0,4 segundo de espera, a atenção começa a vazar.",
      "Abaixo disso a pessoa entra em ritmo com a interface e",
      "produz mais sem perceber."], DOHERTY),
    ("LEI DE MILLER",
     ["A memória de trabalho segura mais ou menos sete coisas.",
      "Agrupar é o truque: três blocos de dois cansam menos",
      "que sete itens soltos na mesma lista."], MILLER),
    ("PREVENÇÃO DE ERROS",
     ["Mensagem de erro boa é a que nunca precisou aparecer.",
      "Validar enquanto a pessoa digita evita o formulário que",
      "só reclama depois de tudo preenchido."], PREVENIR),
    ("EFEITO VON RESTORFF",
     ["O item diferente do resto é o único que fica na memória.",
      "Se tudo está em destaque, nada está. Escolha um botão",
      "para gritar e deixe os outros sussurrarem."], VON_RESTORFF),
    ("LEI DA SIMILARIDADE",
     ["Elementos parecidos são lidos como um conjunto, mesmo",
      "espalhados pela tela. Cor, forma e tamanho agrupam",
      "sem precisar de moldura nem de rótulo."], SIMILARIDADE),
    ("REGRA DO PICO-FIM",
     ["A lembrança de uma experiência não é a média dela.",
      "É o momento mais intenso somado ao final. Capriche na",
      "confirmação do pedido, e não só no formulário."], PICO_FIM),
    ("RECONHECER, NÃO LEMBRAR",
     ["Reconhecer é barato, lembrar é caro.",
      "Deixe as opções à vista em vez de exigir que a pessoa",
      "guarde na cabeça o que viu na tela anterior."], RECONHECER),
    ("LEI DE PRÄGNANZ",
     ["Diante de uma forma complexa, o olho procura a versão",
      "mais simples possível. Formas limpas são entendidas",
      "mais rápido e cansam menos."], PRAGNANZ),
    ("CONTROLE E LIBERDADE",
     ["Gente erra, e erra o tempo todo.",
      "Toda ação precisa de um caminho de volta bem visível:",
      "desfazer, cancelar, sair sem perder o que já foi feito."], DESFAZER),
    ("EFEITO DE POSIÇÃO SERIAL",
     ["De uma lista, ficam o primeiro e o último item.",
      "O que estiver no meio some da memória, então coloque",
      "o que importa nas pontas."], POSICAO_SERIAL),
    ("LEI DA REGIÃO COMUM",
     ["Um contorno em volta cria um grupo na hora, mesmo que",
      "os elementos estejam longe uns dos outros.",
      "É o agrupamento mais forte da Gestalt."], REGIAO_COMUM),
    ("EFEITO ESTÉTICA-USABILIDADE",
     ["Interface bonita é percebida como mais fácil de usar,",
      "mesmo quando o fluxo é idêntico. O capricho visual",
      "compra paciência para os tropeços que sobrarem."], ESTETICA),
    ("NAVALHA DE OCCAM",
     ["Entre duas soluções que resolvem, fique com a mais simples.",
      "Vá tirando elemento até começar a fazer falta:",
      "o que sobrou era o necessário."], OCCAM),
]


def indice(data):
    """Rotação fixa: uma lei por dia, na ordem da lista.

    Usa o número ordinal do dia, que anda de um em um. Assim nenhuma lei
    repete antes de todas as outras terem aparecido, e o ciclo inteiro leva
    exatamente len(LEIS) dias. O sorteio anterior era aleatório com
    reposição: repetia a mesma lei em dias seguidos e deixava outras de fora
    por semanas.
    """
    return data.toordinal() % len(LEIS)


def montar(agora):
    nome, frases, diagrama = LEIS[indice(agora)]
    # o quadro do diagrama comeca em x=600; nome comprido encolhe para nao encostar
    corpo_nome = 30 if len(nome) <= 26 else 25
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
      <text class="sobe s2" x="38" y="104" font-size="{corpo_nome}" font-weight="700" letter-spacing="1.2" fill="{TINTA}">{nome}</text>
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
