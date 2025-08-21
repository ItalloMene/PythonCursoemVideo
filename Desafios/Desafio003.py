# DESAFIO 3 - Crie um programa que leia dois números e mostre a soma entre elas.
cores = {
    'Bold-Verde' : '\033[32m',
    'Bold-Azul' : '\033[34m',
    'Limpar' : '\033[m'
}
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
s = n1 + n2
print('A soma entre {}{}{} e {}{}{} vale {}{}{}.'.format( cores['Bold-Verde'], n1, cores['Limpar'], cores['Bold-Verde'], n2, cores['Limpar'], cores['Bold-Azul'], s, cores['Limpar']))