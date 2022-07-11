#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Curso: Linguagem Python
# Prof. Douglas Machado Tavares

print(".:: Numero de vogais :-) ::.")

frase = input("Digite uma frase: ")
frase = frase.lower()

num_vogais = frase.count("a") + frase.count("e")
num_vogais += frase.count("i") + frase.count("o")
num_vogais += frase.count("u")

print("A frase tem {n} vogais.".format(n=num_vogais))
