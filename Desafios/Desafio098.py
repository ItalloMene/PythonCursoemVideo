"""
Desafio 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo
e realize a contagem.
O seu programa tem que realizar três contagens através da funcão criada:
A) De 1 até 10, de 1 em 1.
B) De 10 até 0, de 2 em 2.
C) Uma contagem personalizada.
"""
from time import sleep

def contador(inicio, fim, cont):
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


contador(1, 10, 1)
print('=-' * 40)
contador(10,0,2)
print('=-' * 40)
começo = int(input('→ Digite o começo da contagem: '))
final = int(input('→ Digite o final da contagem: '))
passo = int(input('→ Digite os passos da contagem: '))
print('=-' * 40)
if passo == 0:
    contador(inicio= começo, fim= final, cont= 1)
else:
    contador(inicio= começo,fim= final,cont= passo)
