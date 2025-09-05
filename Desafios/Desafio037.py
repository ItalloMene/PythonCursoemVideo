"""
Desafio 037 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""
print('=' * 30)
num = int(input('Digite um número: '))
print('=' * 30)
print('Bases de conversão: \n1 - Binário \n2 - Octal \n3 - Hexadecimal')
print('=' * 30)
escolha = int(input('Digite sua escolha: '))
print('=' * 30)

if escolha == 1:
    binario = bin(num)[2:]
    print('O número \033[1;92m{}\033[m em Binário é: \033[1;92m{}\033[m'.format(num, binario))
elif escolha == 2:
    octal = oct(num)[2:]
    print('O número \033[1;92m{}\033[m em Octal é: \033[1;92m{}\033[m'.format(num, octal))
elif escolha == 3:
    hexadecimal = hex(num)[2:]
    print('O número \033[1;92m{}\033[m em Hexadecimal é: \033[1;92m{}\033[m'.format(num, hexadecimal))
else:
    print('\033[1;91mEscolha inválida!\033[m')
    print('Selecione entre as opções 1, 2 ou 3.')
