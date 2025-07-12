# DESAFIO 006 - Crie um programa que leia um número e mostre seu dobro, triplo e raiz quadrada.
numero = float(input('Por favor, digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print('O número digitado é {:.2f}, seu dobro é {:.2f}, seu triplo é {:.2f} e sua raiz é {:.2f}'.format(numero,dobro,triplo,raiz))
