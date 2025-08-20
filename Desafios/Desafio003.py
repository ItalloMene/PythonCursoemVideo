# DESAFIO 3 - Crie um programa que leia dois números e mostre a soma entre elas.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
s = n1 + n2
print('A soma entre {}{}{} e {}{}{} vale {}{}{}'.format('\033[0;32m', n1 ,'\033[m','\033[0;32m',n2,'\033[m','\033[34m',s,'\033[m'))