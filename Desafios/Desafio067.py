"""
Desafio 067: Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""
print('=' * 55)
print(f'{'TABUADA':^55}')
print('=' * 55)
print(' + Digite um número negativo para finalizar o programa.')
print('-' * 55)
while True:
    num = int(input(' → Digite um número: '))
    print('-' * 55)
    if num < 0:
        break
    for cont in range(0,11):
        print(f'{' ':>20} {num} x {cont:2} = {num * cont}')
    print('-' * 55)
print(f'{' ':>15} Fim do programa, volte sempre!')
print('=' * 55)