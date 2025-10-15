"""
Desafio 068: faça um programa que jogue Par ou Impar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo.
"""
from random import randint
print('=' * 35)
print(f'\033[93m{'PAR OU IMPAR':^35}\033[m')
print('=' * 35)
vitoria = 0
while True:
    pensar = randint(1,10)
    while True:
        escolha = str(input(' → Escolha ente Par ou Impar: ')).upper().strip()[0]
        if  escolha in 'PpIi':
            break
    while True:
        num = int(input(' → Escolha um número: '))
        if num >=0:
            break
    print('-' * 35)
    print(f' → Escolha do computador: \033[32m{pensar}\033[m')
    soma = pensar + num
    print(f' → Soma das escolhas: \033[32m{soma}\033[m')
    if soma % 2 == 0:
        print(' → Resultado: PAR')
        if escolha in 'Pp':
            print('-' * 35)
            print(' + JOAGADOR VENCEU!')
            print('-' * 35)
            vitoria += 1
        else:
            print('-' * 35)
            print(' + COMPUTADOR VENCEU!')
            print('-' * 35)
            break
    if soma % 2 == 1:
        print(' → Resultado: IMPAR')
        if escolha in 'Ii':
            print('-' * 35)
            print(' + JOGADOR VENCEU!')
            print('-' * 35)
            vitoria += 1
        else:
            print('-' * 35)
            print(' + COMPUTADOR VENCEU!')
            print('-' * 35)
            break
print(f' → Foram \033[93m{vitoria}\033[m consecutivas do jogador.')
print('=' * 35)