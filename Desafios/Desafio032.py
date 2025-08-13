"""
DESAFIO 032 - Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""
ano = int(input('Por favor digite um ano: '))
print('Analisando...'.format(ano))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('{} é um ano Bissexto!'.format(ano))
else:
    print('{} não é um ano Bissexto!'.format(ano))