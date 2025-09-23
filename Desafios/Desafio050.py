"""
Desafio 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor digitado for impar, desconsidere-o.
"""
print('=' * 45)
print('{}{:^45}{}'.format('\033[96m', 'SOMA DOS PARES', '\033[m'))
print('=' * 45)
soma = 0
for contador in range(1,7):
    numero = int(input('  {}) Por favor digite um número inteiro: '.format(contador)))
    if numero % 2 == 0:
        soma = soma + numero
print('=' * 45)
print('{}{:^45}{}'.format('\033[96m', 'RESULTADO', '\033[m'))
print('    A soma entre os valores pares é: {}{}{}'.format('\033[32m', soma, '\033[m'))
print('=' * 45)