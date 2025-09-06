"""
Desafio 038: Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é o maior
- O segundo valor é o maior
- Não existe valor maior, os dois são iguais
"""
print('+' * 25)
print('  \033[1;92mCOMPARADOR DE NÚMEROS\033[m')
print('+' * 25)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print('')
print('     \033[1;4;92mRESPOSTA\033[m')

if n1 > n2:
    print('O primeiro valor é o maior.\n\033[1;4;95m{}\033[m é maior que \033[1;4;95m{}\033[m'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor é o maior.\n\033[1;4;94m{}\033[m é maior que \033[1;4;94m{}\033[m.'.format(n2, n1))
else:
    print('Não existe valor maior.\n\033[1;4;96m{}\033[m e \033[1;4;96m{}\033[m são valores iguais.'.format(n1, n2))