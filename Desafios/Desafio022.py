'''
DESAFIO 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas;
O nome com todas as letras minúsculas;
Quantas letras ao todo (sem considerar os espaços);
Quantas letras que tem o primeiro nome;
'''

nome = str(input('Digite seu nome completo: '))
print('Seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('A quantidade de letras que tem no seu nome completo: {} letras'.format(len(nome.strip())))
separado = nome.split()
primeironome = separado[0]
print('A quantidade de letras que tem o primeiro nome: {} letras'.format(len(primeironome)))