"""
Desafio 038: Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é o maior
- O segundo valor é o maior
- Não existe valor maior, os dois são iguais
"""
# RESPOSTA 01: ELIF
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior.')
elif n2 > n1:
    print('O SEGUNDO valor é maior. ')
elif n1 == n2:
    print('Os dois valores são IGUAIS.')

# RESPOSTA 02: ELSE
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior.')
elif n2 > n1:
    print('O SEGUNDO valor é o maior.')
else:
    print('Os dois valores são IGUAIS.')