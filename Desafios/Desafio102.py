"""
Desafio 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
o número a calcular e o outro chamado ‘show’, que será um valor lógico (opcional) indicando se será mostrado ou não
na tela o processo de cálculo do fatorial.
"""
import math
from time import sleep

def linha():
    print('=' * 50)

def titulo(msg):
    linha()
    print(f'{msg:^50}')
    linha()

def fatorial(calc, show):
    """
    → Realiza o cálculo fatorial a partir de um valor recebido no parametro calc
    se o parametro 'show' for False retorna apenas o resultado do cálculo fatorial
    se for True mostra o cálculo com o resultado no final
    :param calc: recebe o valor fatorial
    :param show: True ou False
    :return: f'→ O resultado fatorial é: {mult}'
    :return: None
    """
    
    if not show:
        mult = math.factorial(calc)
        sleep(0.5)
        return f'→ O resultado fatorial é: {mult}'
    else:
        mult = 1
        print(f' {calc}! ', end='=')
        while calc >= 1:
            mult *= calc
            if calc == 1:
                print(f'{calc} ', end='=')
                sleep(0.5)
            else:
                print(f' {calc} x', end=' ')
                sleep(0.5)
            calc -= 1
        print(f' {mult}')
        return None


# Programa Principal
titulo('CÁLCULO FATORIAL')

num = int(input('→ Digite o valor fatorial: '))

while True:
    resposta = str(input('→ Deseja ver o cálculo fatorial [S/N]? ')).strip().upper()[0]
    if resposta in 'SN':
        break

if resposta in 'S':
    linha()
    fatorial(num, show=True)
else:
    linha()
    print(fatorial(num, show=False))
linha()