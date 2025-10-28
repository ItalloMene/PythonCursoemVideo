"""
Desafio 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma Tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valore
que estão na Tupla.
"""
from random import randint
numeros = (randint(1,10), randint(1, 10), randint(1, 10),
     randint(1,10), randint(1, 10))
print(f'Eu sorteei os valores {numeros}')
# ou
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}.')
print(f'O menor valor sorteado foi {min(numeros)}.')
