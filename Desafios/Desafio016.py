# DESAFIO 016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
from math import trunc
real = float(input('Digite um número real [x.xx]: '))
inteiro = trunc(real)
print('O número {:.3f} tem a parte inteira {}'.format(real, inteiro))