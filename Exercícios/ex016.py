'''
DESAFIO 016 - Crie um programa que leia um npumero Real qualquer pelo teclado e
mostre na tela sua porção Inteira.
Ex: Digite um número:6.127
O número 6.127 tem a parte Inteira 6.
 '''

'''
# Resposta 01: import geral
import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, math.trunc(num)))
'''

'''
# Resposta 02: import específico
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
'''

# Resposta 03: uso da função interna int()
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))