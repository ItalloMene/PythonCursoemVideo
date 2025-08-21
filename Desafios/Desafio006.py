# DESAFIO 006 - Crie um programa que leia um número e mostre seu dobro, triplo e raiz quadrada.
numero = float(input('Por favor, digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print('O número digitado é \033[1;4;45m{:.2f}\033[m, seu dobro é \033[1;4;42m{:.2f}\033[m, seu triplo é \033[1;4;41m{:.2f}\033[m e sua raiz é \033[1;4;44m{:.2f}\033[m'.format(numero,dobro,triplo,raiz))
