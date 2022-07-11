#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Curso: Linguagem Python
# Prof. Douglas Machado Tavares

print(".:: Índice de Massa Corpórea ::.\n")

entrada = input("Digite a massa (kg): ")
massa = float(entrada)

entrada = input("Digite a altura (m): ")
altura = float(entrada)

imc = massa / altura**2

saida = "IMC = {0:7.2f}"
print(saida.format(imc))
