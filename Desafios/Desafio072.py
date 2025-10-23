"""
Desafio 072: Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. O seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
números = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
           'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
print('=' * 45)
print(f'\033[93m{'NÚMERO POR EXTENSO':^45}\033[m')
print('=' * 45)
while True:
    num = int(input(' + Digite um número entre 0 e 20: '))
    if (num >= 0) and (num <= 20):
        break
print('-' * 45)
print(f' Número escolhido: \033[92m{num}\033[m | Por extenso: \033[92m{números[num]}\033[m')
print('=' * 45)
