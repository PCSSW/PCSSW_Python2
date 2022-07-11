#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Curso: Linguagem Python
# Prof. Douglas Machado Tavares

nome = input("Digite seu nome: ")
nome = nome.title()
nome = nome.replace(" Da ", " da ")
nome = nome.replace(" De ", " de ")

frase = "Oi {fulana}. Tudo bem?"
print(frase.format(fulana=nome))
print("Comigo tudo bem!")
print("Vamos brincar?")
print("Vamos correr?")
print(";-D")
