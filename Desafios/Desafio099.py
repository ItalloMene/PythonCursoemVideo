"""
Desafio 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
O seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
def linha():
    print('=' * 35)

def escreva(msg):
    linha()
    print(f'{msg:^35}')
    linha()

def maior(lista):
    mvalor = 0
    for num in lista:
        if num > mvalor:
            mvalor = num
    escreva(f'O maior valor digitado foi {mvalor}')


# Programa principal
numeros = []

escreva("Analisando Maior Valor")

while True:
    numeros.append(int(input('→ Digite um valor: ')))
    while True:
        resposta = str(input('→ Deseja continuar[S/N]? ')).strip().upper()[0]
        if resposta in 'SN':
            break
    if resposta == 'N':
        break
    linha()

maior(numeros)
