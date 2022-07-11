#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Curso: Linguagem Python
# Prof. Douglas Machado Tavares

print(".:: Índice de Massa Corpórea ::.\n")

massa = float(input("Digite a massa (kg): "))
altura = float(input("Digite a altura (m): "))

imc = massa / altura**2

print("IMC = {0:7.2f}".format(imc))
