"""
Desafio 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo numa lista.
No final mostre:
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves
"""
cadastro = list()
pessoas = list()
cont_pessoas = 0

print('=' * 50)
print(f'{"PESSOAS E PESOS":^50}')
print('=' * 50)

while True:
    pessoas.append(str(input('Digite o nome da pessoa: ')))
    cont_pessoas += 1
    pessoas.append(float(input('Digite o peso (Kg) da pessoa: ')))

    if len(cadastro) == 0:
        maior_peso = menor_peso = pessoas[1]
    else:
        if pessoas[1] > maior_peso:
            maior_peso = pessoas[1]
        if pessoas[1] < menor_peso:
            menor_peso = pessoas[1]

    cadastro.append(pessoas[:])
    pessoas.clear()

    while True:
        resposta = str(input('Deseja continuar (Sim/Não)? ')).strip().upper()[0]

        if resposta in 'SN':
            break
    print('-' * 50)

    if resposta in 'N':
        break

print(f'{"RESULTADOS":^50}')
print('-' * 50)
print(f'A) Foram cadastradas {cont_pessoas} pessoas.')
print(f'B) Pessoas com maior peso ({maior_peso}Kg): ', end='')
for pessoa in cadastro:
    if pessoa[1] == maior_peso:
        print(f'{pessoa[0]};', end='')
print()

print(f'C) Pessoas com menor peso ({menor_peso}Kg): ', end='')
for pessoa in cadastro:
    if pessoa[1] == menor_peso:
        print(f'{pessoa[0]};', end='')
print()
print('=' * 50)
