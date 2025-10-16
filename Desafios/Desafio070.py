"""
Desafio 070: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1.000,00
C) Qual é o nome do produto mais barato.
"""
total = produtomil = contador = valmaisbarato = 0
maisbarato = ' '
print('=' * 50)
print(f'\033[96m{'REGISTRO DE COMPRAS':^50}\033[m')
print('=' * 50)
while True:
    produto = str(input(' → Digite o nome do produto: '))
    valor = float(input(' → Digite o valor do produto R$[x.xx]: R$'))
    # soma dos valores dos produtos
    total += valor
    # Registro do produto mais barato
    contador += 1
    if contador == 1:
        maisbarato = produto
        valmaisbarato = valor
    elif valor < valmaisbarato:
        maisbarato = produto
        valmaisbarato = valor
    # Contador de produtos acima de R$1000
    if valor > 1000:
        produtomil += 1
    # Looping para quando a Resposta for igual a S ou N
    while True:
        continuar = str(input(' → Deseja continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'SsNn':
            break
    print('-' * 50)
    # Looping para quando Resposta for igual a N
    if continuar in 'Nn':
        break
print(f'\033[96m{'RESULTADOS':^50}\033[m')
print('-' * 50)
print(f' → Total gasto na compra: R${total:.2f};')
print(f' → Total produtos acima de R$1000,00: {produtomil};')
print(f' → O produto mais barato: {maisbarato};')
print('=' * 50)
