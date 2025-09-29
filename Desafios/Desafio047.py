"""
Desafio 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""
from time import sleep
print('=' * 30)
print('{}{:^30}{}'.format('\033[1;94m','CONTADOR DE PARES', '\033[m'))
print('=' * 30)
for cont in range(2, 51, 2):
    print('{}{:^30}{}'.format('\033[96m', cont, '\033[m'))
    sleep(0.5)
print('=' * 30)
print('{}{:^30}{}'.format('\033[1;94m', 'FIM', '\033[m'))
print('=' * 30)