"""
DESAFIO 036 - Escreva um programa para aprovar o empréstimo bancário
para compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar. Calcule o valor
da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.
"""
texto = {
    'Negrito' : '\033[1m',
    'Roxo' : '\033[1;95m',
    'Amarelo' : '\033[93m',
    'Vermelho' : '\033[1;91m',
    'Ciano' : '\033[96m',
    'Verde' : '\033[1;92m',
    'Limpar' : '\033[m'
}

from time import sleep
valorcasa = float(input('Qual o valor da casa desejada? R$'))
salario = float(input('Por favor digite o salário do comprador: R$'))
anos = int(input('Em quantos anos o comprador irá pagar? '))

prestacao = valorcasa / (anos * 12)
porcentagem = salario * (30/100)

sleep(0.3)
print(' ')
print('{}ANALISANDO...'.format(texto['Roxo']))
print(' ')
sleep(0.5)

if prestacao > porcentagem :
    print('{}='.format(texto['Amarelo']) * 20)
    print('{} EMPRÉSTIMO NEGADO!'.format(texto['Vermelho']))
    print('{}='.format(texto['Amarelo']) * 20)
    print('Valor da prestação excedeu 30% do salário.')
    print('Prestação: {}R${:.2f}{} | 30% do salário: {}R${:.2f}'
          .format(texto['Vermelho'], prestacao, texto['Amarelo'], texto['Vermelho'], porcentagem))
else:
    print('{}+'.format(texto['Ciano']) * 22)
    print('{} EMPRÉSTIMO APROVADO!'.format(texto['Verde']))
    print('{}+'.format(texto['Ciano']) * 22)
    print('Valor da prestação abaixo dos 30% do salário.')
    print('Prestação: {}R${:.2f}{} | 30% do salário: {}R${:.2f}'.format(texto['Verde'],prestacao, texto['Ciano'], texto['Verde'],porcentagem))