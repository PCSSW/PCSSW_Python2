#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Curso: Linguagem Python
# Prof. Douglas Machado Tavares

print(".:: No bar :-) ::.")

resposta = "sim"
while resposta in "sim":
    resposta = input("Mais uma cerveja? [sim/não]: ")
    resposta = resposta.lower()
    if resposta in "sim":
        print("Bebendoooo...")

print("Caasaaaaa")
