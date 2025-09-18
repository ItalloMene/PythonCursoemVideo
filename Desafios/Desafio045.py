"""
Desafio 045 - Crie um programa que faça o computador jogar Jokenpô com você.
"""
from random import choice
from time import sleep
texto = {
    'Ciano' : '\033[96m',
    'Azul' : '\033[94m',
    'Vermelho' : '\033[91m'
}

print('{}='.format(texto['Ciano']) * 40)
print('{}{:^40}{}'.format(texto['Azul'], 'JOKENPÔ' ,texto['Ciano']))
print('='.format(texto) * 40)
sleep(0.8)
# 1 - Pedra, 2 - Papel, 3 - Tesoura
opcao = [1, 2, 3]
computador = choice(opcao)
print(' {} 1 - Pedra | 2 - Papel | 3 - Tesoura {}'.format(texto['Azul'], texto['Ciano']))
jogador= int(input(' > Selecione entre 1, 2 ou 3: '))
print('=' * 40)
sleep(0.8)
if (jogador < 1) or (jogador > 3):
    print(' {}Jogada Inválida! \n Tente novamente entre 1, 2 e 3.{}'.format(texto['Vermelho'], texto['Ciano']))
    print('=' * 40)
else:
    if (jogador == 1) and (computador == 1):
        print(' {}PEDRA VS PEDRA \n Empate entre Jogador e Computador!{}'.format(texto['Azul'], texto['Ciano']))
        print('=' * 40)
    elif (jogador == 2) and (computador == 2):
        print(' {}PAPEL VS PAPEL \n Empate entre jogador e Computador!{}'.format(texto['Azul'], texto['Ciano']))
        print('=' * 40)
    elif (jogador == 3) and (computador == 3):
        print(' {}TESOURA VS TESOURA \n Empate entre jogador e Conputador!{}'.format(texto['Azul'], texto['Ciano']))
        print('=' * 40)
    elif (jogador == 1) and (computador == 2):
        print(' {}PEDRA VS PAPEL \n Vitória do Computador!{}'.format(texto['Azul'], texto['Ciano']))
        print('=' * 40)
    elif (jogador == 1) and (computador == 3):
        print(' {}PEDRA VS TESOURA \n Vitória Jogador!{}'.format(texto['Azul'], texto['Ciano']))
        print('=' * 40)
    elif (jogador == 2) and (computador == 3):
        print(' {}PAPEL VS TESOURA \n Vitória Computador!{}'.format(texto['Azul'], texto['Ciano']))
        print('=' * 40)
    elif (jogador == 2) and (computador == 1):
        print(' {}PAPEL VS PEDRA \n Vitória Jogador!{}'.format(texto['Azul'], texto['Ciano']))
        print('=' * 40)
    elif (jogador == 3) and (computador == 1):
        print(' {}TESOURA VS PEDRA \n Vitória Computador!{}'.format(texto['Azul'], texto['Ciano']))
        print('=' * 40)
    elif (jogador == 3) and (computador == 2):
        print(' {}TESOURA VS PAPEL \n Vitória Jogador!{}'.format(texto['Azul'], texto['Ciano']))
        print('=' * 40)
    else:
        print('{}[ERRO] Não foi possível analisar as jogadas!{}'.format(texto['Vermelho'], texto['Ciano']))
        print('=' * 40)