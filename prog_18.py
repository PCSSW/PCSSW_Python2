#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Curso: Linguagem Python
# Prof. Douglas Machado Tavares

print(".:: No bar :-) ::.")

while True:
    resposta = input("Mais uma cerveja? [sim/não]: ")
    resposta = resposta.lower()
    if resposta in ["sim", "mais", "mais uma", "beleza", "ok"]:
        print("Bebendoooo...")
    else:
        break

print("Caasaaaaa")
