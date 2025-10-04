"""
Desafio058: melhore o jogo do Desafio028 onde o computador vai "pensar" num número de 0 a 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
"""
from random import randint

print('=' * 50)
print('{:^50}'.format('ACERTE O NÚMERO'))
print('=' * 50)

print(' Olá jogador! '
      '\n Que tal adivinhar em qual número estou pensando?')
print('-' * 50)

pensar = randint(0, 10)
palpite = 0
tentativa = 0

while pensar != palpite:
    palpite = int(input('→ Digite um palpite entre 0 e 10: '))
    print('-' * 50)
    tentativa += 1

print(' PARABÉNS VOCÊ ACERTOU! '
      '\n O computador pensou em {} e seu palpite foi {}.'.format(pensar, palpite))
print('-' * 50)
print(' Foram necessário {} tentativas até acertar!'.format(tentativa))
print('=' * 50)