#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Curso: Linguagem Python
# Prof. Douglas Machado Tavares

print(":: For  vs  While ::".center(60, '.'))

print("For in")
turma = [4, 5, 1, 2, 9, 3]
for nota in turma:
    print(nota * 1.25)
print("Ufa!!!")

print("\nWhile")
turma = [4, 5, 1, 2, 9, 3]
i = 0
while i < len(turma):
    nota = turma[i]
    print(nota * 1.25)
    i = i + 1
print("Ufa!!!")
