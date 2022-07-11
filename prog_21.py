#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Curso: Linguagem Python
# Prof. Douglas Machado Tavares

print("...:: Aviario S.T. ::...\n")

galinheiro_G1 = [3.200, 2.980, 3.100, 2.800,
                 3.450, 3.210, 2.970, 3.050]

media = sum(galinheiro_G1) / len(galinheiro_G1)
maior = max(galinheiro_G1)
menor = min(galinheiro_G1)

print(" Média: {0:.3f} kg".format(media))
print("Máxima: {0:.3f} kg".format(maior))
print("Mínima: {0:.3f} kg".format(menor))
