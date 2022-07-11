#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Curso: Linguagem Python
# Prof. Douglas Machado Tavares

print("...:: Aviario S.T. ::...\n")

galinheiro_G1 = [3.200, 2.980, 3.100, 2.800,
                 3.450, 3.210, 2.970, 3.050]

soma = 0.0
for massa in galinheiro_G1:
    soma = soma + massa
media = soma / len(galinheiro_G1)

maior = galinheiro_G1[0]
for massa in galinheiro_G1:
    if massa > maior:
        maior = massa

menor = galinheiro_G1[0]
for massa in galinheiro_G1:
    if massa < menor:
        menor = massa

print(" Média: {0:6.3f} kg".format(media))
print("Máxima: {0:6.3f} kg".format(maior))
print("Mínima: {0:6.3f} kg".format(menor))
