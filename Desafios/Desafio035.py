"""
DESAFIO 035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.
"""
reta1 = int(input('Digite o comprimento da primeira reta: '))
reta2 = int(input('Digite o comprimento da segunda reta: '))
reta3 = int(input('Digite o comprimento da terceira reta: '))
print(' ')
print('| reta 1: {} | reta 2: {} | reta 3: {} |'.format(reta1, reta2, reta3))

if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print('Com essas retas é possível formar um Triângulo.')
else:
    print('Com essas retas não é possível formar um Triângulo.')