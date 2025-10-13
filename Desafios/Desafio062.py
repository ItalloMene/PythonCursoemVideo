"""
Desafio 062 - Melhore o Desafio061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""
print('=' * 50)
print('{:^50}'.format(' PROGRESSÃO ARITMÉTICA 3'))
print('=' * 50)
termo1 = int(input(' → Digite o primeiro termo da PA: '))
razao = int(input(' → Digite a razão da PA: '))
print('-' * 50)
contador = 1
while contador <= 10:
    termo = termo1 + contador * razao
    print('{}º Termo = {}'.format(contador, termo))
    contador += 1
    print('-' * 50)
quantidade = 1
ultimotermo = 11
while (quantidade != 0) and (quantidade > 0):
    quantidade = int(input(' → Digite quantos termos a mais deseja ver: '))
    print('-' * 50)
    novostermos = quantidade + ultimotermo
    for c in range(ultimotermo, novostermos):
        termo = termo1 + c * razao
        print('{}º Termo = {}'.format(c, termo))
        print('-' * 50)
    ultimotermo = novostermos
print(' → Fim do programa!')
print('-' * 50)

