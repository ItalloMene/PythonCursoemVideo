"""
Desafio 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa perguntará quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo numa lista composta.
"""
from random import randint
from time import sleep

texto = {
    'Azul' : '\033[1;94m',
    'Bolder': '\033[1m',
    'Limpar' : '\033[m'
}

print(f'{texto['Azul']}=' * 40)
print(f'{"PALPITES MEGA SENA":^40}')
print('=' * 40, texto['Limpar'])

palpites = list()
jogos = list()

quantidade = int(input(f'{texto['Bolder']} → Quantos jogos serão gerados? '))


for cont in range(0, quantidade):
    for val in range(0, 6):
        while True:
            escolha = randint(1, 60)
            if escolha not in jogos:
                break
        jogos.append(escolha)
    palpites.append(jogos[:])
    jogos.clear()

for cont in range(0, len(palpites)):
    sleep(1)
    print('-' * 40)
    print(f'{texto['Bolder']} → Jogo {cont + 1} = {palpites[cont]}{texto['Limpar']}')
print(f'{texto['Azul']}=' * 40, texto['Limpar'])
