"""
DESAFIO 027 - Faça um programa que leia o nome completo de uma pessoa.
Mostrando em seguida o primeiro e o último nome separadamente
Ex: Ana Maria de Souza
primeiro = Ana | ultimo = Souza
"""

nome = str(input('Digite seu nome por favor: '))
dividido = nome.split()
primeiro = dividido[0]
ultimo =  dividido[-1]
print(nome)
print('Primeiro nome = {} | Ultimo nome = {}'.format(primeiro,ultimo))
