"""
Desafio 048: Faça um programa que calcule a soma entre todos os números ímpares
que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.
"""
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        # #acumulador - normalmente soma um valor
        soma += c #mesmo que: soma = soma + c
        # #contador - normalmente soma 1
        cont += 1 #mesmo que: cont = cont + 1
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))
