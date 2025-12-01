"""
Desafio 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo
e realize a contagem.
O seu programa tem que realizar três contagens através da funcão criada:
A) De 1 até 10, de 1 em 1.
B) De 10 até 0, de 2 em 2.
C) Uma contagem personalizada.
"""
from time import sleep

def linha():
    print('-=' * 40)
def contador(inicio, fim, cont):
    print(f'Contagem de {inicio} até {fim} de {cont} em {cont}:')
    if inicio < fim:
        for cont in range(inicio, fim + 1, cont):
            print(cont, end=' → ')
            sleep(0.5)
        print('FIM!')
    elif inicio > fim:
        for cont in range(inicio, fim-1, -cont):
            print(cont, end=' → ')
            sleep(0.5)
        print('FIM!')


linha()
contador(1, 10, 1)
linha()
contador(10,0,2)
linha()
começo = int(input('→ Digite o começo da contagem: '))
final = int(input('→ Digite o final da contagem: '))
passo = int(input('→ Digite os passos da contagem: '))
linha()
if passo == 0:
    contador(inicio= começo, fim= final, cont= 1)
elif passo < 0:
    passo *= -1
    contador(inicio= começo, fim=final, cont= passo)
else:
    contador(inicio= começo,fim= final,cont= passo)
linha()
