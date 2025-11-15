"""
Desafio 091: Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios
Guarde esses resultados num dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o
maior número do dado.
"""
from random import randint
from time import sleep
jogadores = {'Jogador1': randint(1,6),
             'Jogador2':randint(1, 6),
             'Jogador3':randint(1,6),
             'Jogador4':randint(1,6)}
print('-=' * 20)
print(f'{"VALORES SORTEADOS":^40}')
print('=-' * 20)
for chave, valor in jogadores.items():
    print(f'→ {chave} tirou {valor}')
    sleep(1)
print('-=' * 20)
print(f'{"RANKING DOS JOGADORES":^40}')
print('-=' * 20)
ranking = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
cont = 0
for chave, valor in ranking.items():
    cont += 1
    print(f'{cont}º lugar: {chave} com {valor}')
    sleep(1)
print('=-' * 20)
print(jogadores)
print(ranking)
