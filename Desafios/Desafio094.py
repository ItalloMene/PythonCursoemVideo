"""
Desafio 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
os dados de cada pessoa em dicionário e todos os dicionários numa lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média
"""
grupo = []
print('=' * 40)
while True:
    nome = str(input(' → Nome: '))
    while True:
        sexo = str(input(' → Sexo [M/F]: ')).strip().upper()[0]
        if sexo in 'MF':
            break
    idade = int(input(' → Idade: '))
    while True:
        resposta = str(input(' → Quer continuar [S/N]? ')).strip().upper()[0]
        if resposta in 'SN':
            break
    print('-' * 40)
    pessoas = {'nome':nome, 'sexo':sexo, 'idade':idade}
    grupo.append(pessoas.copy())
    pessoas.clear()
    if resposta in 'Nn':
        break

quant_pessoas = soma_idades = 0
for item in grupo:
    quant_pessoas += 1
    soma_idades += item['idade']
media_idades = soma_idades / quant_pessoas

print(f'{"RESULTADOS":^40}')
print('=' * 40)
print(f' A) O grupo tem {quant_pessoas} pessoas.')
print(f' B) A média de idade é de {media_idades:.2f} anos')
print(f' C) As mulheres do grupo são: ', end='')
for pessoa in grupo:
    if pessoa['sexo'] in 'F':
        print(f'{pessoa['nome']};', end=' ')
print()
print(f' D) Pessoas com idade acima da média: ')
for pessoa in grupo:
    if pessoa['idade'] > media_idades:
        print(f' → Nome = {pessoa['nome']}; Sexo = {pessoa['sexo']}; Idade = {pessoa['idade']};')
print('=' * 40)
print(f'{"FIM DO PROGRAMA":^40}')
print('=' * 40)
#print(grupo)
