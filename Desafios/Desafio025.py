'''
DESAFIO 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome.
'''
nome = str(input('Digite seu nome, por favor: '))
Nome = nome.title()
encontrar = 'Silva' in Nome
print('Verificando se há "Silva" no nome digitado...')
print('Resultado: {}'.format(encontrar))