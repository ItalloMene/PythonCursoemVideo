"""
Desafio 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
"""
from operator import truediv

print('=+' * 15)
print('{:^30}'.format('DESCOBRINDO NÚMERO PRIMO'))
print('+=' * 15)
número = int(input('Por favor Digite um número: '))
print('=' * 30)
print('{:^30}'.format('RESULTADO'))
print('=' * 30)
if número <= 1:
    print('{:^5}{} NÃO É PRIMO!'.format('',número))
    print('=' * 30)
else:
    primo = True
    for contador in range(2, número):
        if número % contador == 0:
            primo = False
    if primo:
        print('{:^5}{} é NÚMERO PRIMO!'.format('',número))
        print('=' * 30)
    else:
        print('{:^5}{} NÃO é NÚMERO PRIMO!'.format('',número))
        print('=+' * 15)

