"""
DESAFIO 028 - Escreva um programa que faça o computador "pensar" num número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.
    + O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
import random
pensar = random.randint(0,5)
print('Olá jogador, que tal adivinhar em qual o computador está pensando? ')
palpite = int(input('Por favor, digite um número entre 0 e 5: '))
print('O computador pensou no número: {}'.format(pensar))
if palpite == pensar:
    print('Parabéns você acertou o palpite, então você Venceu!')
else:
    print('Infelizmente você errou o palpite, então você perdeu.')
