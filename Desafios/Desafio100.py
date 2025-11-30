"""
Desafio 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores pares sorteados pela função anterior.
"""
from random import randint
from time import sleep

numeros = list()

def linha():
    print('=' * 65)

def cabeçalho():
    linha()
    print(f'{"SORTEIO SOMA PARES":^65}')
    linha()

def sorteia():
    for c in range(0, 6):
        numeros.append(randint(0,100))
    print('→ Os números sorteados são: ', end='')
    for val in numeros:
        print(val, end=' → ')
        sleep(0.75)
    print('FIM!')

def somaPar(lista):
    soma = 0
    for val in lista:
        if val % 2 == 0:
            soma += val
    linha()
    print(f'→ E a soma entre os valores pares é: {soma}')
    linha()

# Programa principal
cabeçalho()
sorteia()
sleep(1)
somaPar(numeros)
