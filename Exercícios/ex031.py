"""
DESAFIO 031 - Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando $0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas
"""
from PythonCursoemVideo.Desafios.Desafio031 import distancia

# RESPOSTA 01: Condicional Composta
'''distância = float(input('Qual é a distância de sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))'''

# RESPOSTA 02: If Simplificado
distância = float(input('Qual é a distÂncia de sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distância))
preço = distância = 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
