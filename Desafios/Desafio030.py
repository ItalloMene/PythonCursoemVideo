"""
DESAFIO 030 - Crie um programa que leia um número inteiro e mostre se ele é PAR ou IMPAR.
"""
num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é IMPAR!'.format(num))