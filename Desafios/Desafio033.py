"""
DESAFIO 033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor
"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print(' ')

print('Analisando os números: {}, {}, {}.'.format(n1, n2, n3))
if n1 > n2 and n1 > n3:
  print('O primeiro número ({}) é o maior número entre os demais.'.format(n1))
else:
    if n2 > n1 and n2 > n3:
        print('O segundo número ({}) é o maior número entre os demais.'.format(n2))
    else:
        if n3 > n1 and n3 > n2:
            print('O terceiro número ({}) é o maior número entre os demais'.format(n3))


if n1 < n2 and n1 < n3:
    print('O primeiro número ({}) é o menor número entre os demais.'.format(n1))
else:
    if n2 < n1 and n2 < n3:
        print('O segundo número ({}) é o menor número entre os demais.'.format(n2))
    else:
        if n3 < n1 and n3 < n2:
            print('O terceiro número ({}) é o menor número entre os demais.'.format(n3))

if n1 == n2 and n1 == n3 and n2 == n3:
    print('Números iguais encontrados, não há maior ou menor entre eles.')
