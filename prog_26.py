#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Curso: Linguagem Python
# Prof. Douglas Machado Tavares

print(".:: Quadrado ::.\n")

lado = int(input("Digite o lado: "))

desenho = ""
linha = 1
while linha <= lado:
    coluna = 1
    while coluna <= lado:
        desenho = desenho + "#"
        coluna = coluna + 1
    desenho = desenho + "\n"
    linha = linha + 1

print("")
print(desenho)
