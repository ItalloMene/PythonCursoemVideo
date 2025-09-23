"""
Desafio 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
print('=' * 35)
print('{:^35}'.format('PROGRESSÃO ARITMÉTICA'))
print('=' * 35)
primeiro_termo = int(input(' + Digite o primeiro termo da PA: '))
razão = int(input(' + Digite a razão da PA: '))
print('-' * 35)
print('{:^35}'.format('RESULTADO'))
print('-' * 35)
for contador in range(1, 11):
    termo = primeiro_termo + contador * razão
    print('{:^11}{:2}ºTermo: {}'.format(' ',contador, termo))
print('=' * 35)