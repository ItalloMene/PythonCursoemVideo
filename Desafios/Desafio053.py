"""
Desafio 053: Crie um programa que leia uma frase qualquer e diga se ela é um PALINDROMO,
desconsiderando os espaços.
"""
from time import sleep
print('=' * 30)
print('{:^30}'.format('É PALINDROMO OU NÃO?'))
print('=' * 30)
frase = str(input(' > Digite uma frase:\n '))
semespaço = frase.replace(' ','').lower()
print('-' * 30)
sleep(1)
print('{:^30}'.format('Avaliando...'))
print('-' * 30)
sleep(1)
print('{:^30}'.format('RESULTADO'))
print('-' * 30)
if semespaço == semespaço[::-1]:
    print('  > É um PALÍNDROMO!')
    print('=' * 30)
else:
    print('  > Não é um PALÍNDROMO!')
    print('=' * 30)

