#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Curso: Linguagem Python
# Prof. Douglas Machado Tavares

print(":: Conversor de m/s para km/h ::".center(80, "."))

entrada = input("Digite a velocidade (m/s): ")

vms = float(entrada)
vkmh = vms * 3.6

saida = "{v_entrada:+9.3f} m/s = {v_saida:+9.3f} km/h"
print(saida.format(v_entrada=vms, v_saida=vkmh))
