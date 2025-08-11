"""
DESAFIO 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "SANTO"
"""
cidade = str(input('Por favor, digite o nome de uma cidade: '))
maiusculo = cidade.upper()
separado = maiusculo.split()
teste = 'SANTO' in separado[0]
print('Verificando se há "SANTO" na cidade digitada...')
print('Resultado: {}'.format(teste))
