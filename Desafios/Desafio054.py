"""
Desafio 054: Crie um programa que leia o ano de nascimento de sete pessoas.
No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
(Considerar 21 anos como maior idade)
"""
from datetime import date
print('=' * 55)
print('{:^55}'.format('MAIOR OU MENOR IDADE'))
print('=' * 55)
maior = 0
menor = 0
ano_atual = date.today().year
for contador in range(1,8):
    nascimento = int(input("{}ª Pessoa, por favor digite seu ano de nascimento: ".format(contador)))
    if nascimento <= 0:
        print('[ERRO] Não foi possível verificar o ano de nascimento.')
    else:
        idade = ano_atual - nascimento
        if idade >= 21:
            maior = maior + 1
            print('Idade: {} anos.'.format(idade))
            print('-' * 55)
        elif idade < 21:
            menor = menor + 1
            print('Idade: {} anos'.format(idade))
            print('-' * 55)
print('{:^55}'.format('RESULTADO'))
print('-' * 55)
print('{} pessoas atingiram a maior idade. \n{} pessoas ainda não atingiram a maior idade.'.format(maior, menor))
print('=' * 55)
