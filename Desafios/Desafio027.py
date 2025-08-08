'''
DESAFIO 027 - Faça um programa que leia o nome completo de uma pessoa.
mostrando em seguida o primeiro e o ultimo nome separadamente
Ex: Ana Maria de Souza
primeiro = Ana | ultimo = Souza
'''
from traceback import print_tb

nome = str(input('Digite seu nome por favor: '))
dividido = nome.split()
primeiro = dividido[0]
ultimo =  dividido[-1]
print(nome)
print('Primeiro nome = {} | Ultimo nome = {}'.format(primeiro,ultimo))
