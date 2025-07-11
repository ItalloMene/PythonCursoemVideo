# DESAFIO 006 - Crie um programa que leia um número e mostre seu dobro, triplo e raiz quadrada.
numero = float(input('Por favor, digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero * (1/2)
print('O número digitado é {:.3}, seu dobro é {:.3}, seu triplo é {:.3} e sua raiz é {:.3}'.format(numero,dobro,triplo,raiz))
