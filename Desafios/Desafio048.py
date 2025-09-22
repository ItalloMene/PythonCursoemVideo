"""
Desafio 048: Faça um programa que calcule a soma entre todos os números ímpares
que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.
"""
from time import sleep
print('+' * 40)
print(' SOMANDO NÚMEROS ÍMPARES MÚLTIPLOS DE 3')
print('+' * 40)
sleep(1)
print(' Contando de 1 a 500...')
soma = 0
for cont in range(1,501):
    if (cont % 2 == 1) and (cont % 3 == 0):
        soma = soma + cont
print('+' * 40)
sleep(2)
print(' O resultado da soma é: {}{}{}'.format('\033[4;92m', soma, '\033[m'))
print('+'* 40)