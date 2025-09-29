"""
Desafio 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""
# RESPOSTA 01: Utilizando if (Mais iterações)
for n in range (1, 51):
    print('.', end = '')
    if n % 2 == 0:
        print(n, end = ' ')
print('Acabou')
# RESPOSTA 02: Utilizando passo do for (Menos Iterações)
for n in range(2, 51, 2):
    print('.', end = '')
    print(n, end=' ')
print('Acabou')