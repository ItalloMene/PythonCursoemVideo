"""
DESAFIO 031 - Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando $0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas
"""
distancia = int(input('Quantos km de distância tem sua viagem? '))
if distancia < 200:
    valor = distancia * 0.50
    print('O preço da sua passagem é R${:.2f}.'.format(valor))
else:
    valor = distancia * 0.45
    print('O preço da sua passagem é R${:.2f}.'.format(valor))

