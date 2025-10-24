"""
Desafio 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma Tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valore
que estão na Tupla.
"""
from random import randint

menor = maior = n1 = randint(1,10)

for cont in range (1, 5):
    escolha = randint(1,10)
    if escolha > maior:
        maior = escolha
    if escolha < menor:
        menor = escolha
    if cont == 1:
        n2 = escolha
    elif cont == 2:
        n3 = escolha
    elif cont == 3:
        n4 = escolha
    elif cont == 4:
        n5 = escolha

numeros = (n1, n2, n3, n4, n5)
print('-' * 50)
print(f'{'RESULTADO':^50}')
print('-' * 50)
print(f' → Lista de números gerada: {numeros}.')
print(f' + O maior número dessa lista: {maior}.')
print(f' - O menor número dessa lista: {menor}.')
print('-' * 50)