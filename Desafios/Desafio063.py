"""
Desafio063 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
de uma sequência Fibonecci.
Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""
print('=' * 50)
print('{:^50}'.format(' FIBONACCI'))
print('=' * 50)
n = int(input(' → Digite quantos termos quer ver: '))
print('-' * 50)
termo1 = 0
termo2 = 1
print(' {} → {} → '.format(termo1, termo2), end='')
cont = 3
while cont <= n:
    termo3 = termo1 + termo2
    print('{} → '.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print('Fim')
print('=' * 50)
