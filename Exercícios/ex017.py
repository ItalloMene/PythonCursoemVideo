'''DESAFIO 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triâmgulo retângulo, calcule o mostre o comprimento da hipotenusa.'''

'''
# RESPOSTA 01: Por Operadores / Maneira matemática
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h1 =  (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}.'.format(h1))
'''

'''
# RESPOSTA 02: Função Math geral / Maneira "simples"
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''

# RESPOSTA 03: Função Math especifico
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}.'.format(hi))