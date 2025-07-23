# DESAFIO 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triâmgulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
import math
catoposto = float(input('Digite o comprimento do cateto oposto: '))
catadjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa =  math.sqrt(math.pow(catoposto,2) + math.pow(catadjacente, 2))
print('O comprimento da Hipotenusa é {:.2f}.'.format(hipotenusa))