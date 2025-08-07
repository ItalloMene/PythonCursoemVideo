'''
DESAFIO 023 - Faça um programa que leia um número de 0 a 9999 e
mostre cada um dos digitos separados.
Ex: Digite um número: 1834
unidade:4 dezena:3 centena:8 milhar:1
'''
num = str(input('Digite um número de 0000 a 9999 (sem espaços): '))
print('| Unidade: {} | Dezena: {} | Centena: {} | Milhar: {} |'.format(num[3], num[2], num[1], num[0]))

