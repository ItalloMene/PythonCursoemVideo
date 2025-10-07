"""
Desafio061 - Refaça o Desafio051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
print('=' * 40)
print('{:^40}'.format('PROGRESSÃO ARITMÉTICA'))
print('=' * 40)
primeiro_termo = int(input(' → Digite o primeiro termo da PA: '))
razao = int(input(' → Digite a razão da PA: '))
print('-' * 40)
print('{:^40}'.format('RESULTADO'))
print('=' * 40)
contador = 1
while contador <= 10:
    termo = primeiro_termo + contador * razao
    print('{:^12}{:2}º Termo = {}'.format(' ', contador, termo))
    contador += 1
print('=' * 40)
