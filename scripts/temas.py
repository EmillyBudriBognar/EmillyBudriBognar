#!/usr/bin/env python3
"""Gera os dois temas de cada peça a partir de um único arquivo-mestre.

Cada SVG em `assets/src/` é escrito no tema CLARO (o padrão da marca, igual ao
budri.com.br). Este script troca os tokens de cor de uma vez só e grava:

    assets/<nome>.svg        → tema claro   (fallback do <picture>)
    assets/<nome>-dark.svg   → tema escuro

Cores fora do dicionário passam intactas de propósito: é assim que a faixa
roxa do marquee, o glow e as bolhas coloridas ficam iguais nos dois temas.
"""

import os
import re

TOKENS = {
    # fundos e superfícies
    "#faf5ff": "#150b28",   # fundo base
    "#f3e8ff": "#1e1039",   # fundo 2
    "#fffdff": "#251749",   # superfície do card
    "#f5f0fe": "#2a1850",   # trilho / inset
    "#e9d5ff": "#3b2366",   # linhas e bordas

    # tinta
    "#111827": "#f7f5ff",   # texto forte (e o contorno preto das bolhas)
    "#4b5563": "#b8b0d6",   # texto suave
    "#6b7280": "#8d85ac",   # texto discreto

    # marca
    "#6b21a8": "#e9d5ff",   # roxo forte
    "#7e22ce": "#c084fc",   # roxo
    "#9333ea": "#a855f7",   # roxo da marca
    "#c084fc": "#d8b4fe",   # roxo claro

    # semânticas
    "#2563eb": "#60a5fa",
    "#db2777": "#f472b6",
    "#16a34a": "#4ade80",
    "#ea580c": "#fb923c",
    "#ca8a04": "#facc15",

    # escala de calor do calendário de contribuições
    "#f0e6fd": "#241645",
    "#ddc7fb": "#3d2168",
    "#c08bf5": "#6d35b8",
    "#9b4dee": "#a05ef0",
}

_PADRAO = re.compile("|".join(sorted(TOKENS, key=len, reverse=True)), re.IGNORECASE)


def escurecer(svg):
    """Troca todos os tokens de uma vez - nunca em cascata."""
    return _PADRAO.sub(lambda m: TOKENS[m.group(0).lower()], svg)


def gravar(nome, svg_claro, raiz=None):
    raiz = raiz or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    destino = os.path.join(raiz, "assets")
    os.makedirs(destino, exist_ok=True)
    for sufixo, conteudo in ((".svg", svg_claro), ("-dark.svg", escurecer(svg_claro))):
        caminho = os.path.join(destino, nome + sufixo)
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo)
    return nome


def main():
    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    origem = os.path.join(raiz, "assets", "src")
    if not os.path.isdir(origem):
        raise SystemExit(f"pasta de mestres nao encontrada: {origem}")

    feitos = []
    for arquivo in sorted(os.listdir(origem)):
        if not arquivo.endswith(".svg"):
            continue
        with open(os.path.join(origem, arquivo), encoding="utf-8") as f:
            feitos.append(gravar(arquivo[:-4], f.read(), raiz))
    print(f"{len(feitos)} pecas em dois temas: {', '.join(feitos)}")


if __name__ == "__main__":
    main()
