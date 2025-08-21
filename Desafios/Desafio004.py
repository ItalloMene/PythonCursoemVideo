# DESAFIO 4 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
cores = {
    'bold' : '\033[1m',
    'vermelho' : '\033[1;31m',
    'amarelo' : '\033[1;33m',
    'verde' : '\033[1;32m',
    'ciano' : '\033[1;36m',
    'azul' : '\033[1;34m',
    'limpar' : '\033[m'
}

val = input('{}Por favor, digite algo:'.format(cores['bold']))
print(type(val))
print( cores['vermelho'], 'tem apenas letras?', val.isalpha(), cores['limpar'])
print( cores['amarelo'], 'tem apenas números?', val.isnumeric(), cores['limpar'])
print( cores['verde'], 'tem letras e/ou números?', val.isalnum(), cores['limpar'])
print( cores['ciano'], 'tem apenas letras maiúsculas?', val.isupper(), cores['limpar'])
print( cores['azul'],'tem apenas letras minúsculas?', val.islower(), cores['limpar'])
