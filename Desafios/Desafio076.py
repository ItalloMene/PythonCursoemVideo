"""
Desafio 076: Crie um programa que crie uma tupla única com nomes de produtos e os seus respectivos preços, na sequência.
No final mostre uma listagem de preços organizado, dados em forma tabular
"""
cores = {
    'Título' : '\033[96m',
    'Valor' : '\033[92m',
    'Produto' : '\033[97m',
    'Limpar' : '\033[m'
}

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('=' * 40)
print(f'{cores['Título']}{'LISTAGEM DE PREÇOS':^40}{cores['Limpar']}')
print('=' * 40)
for cont in range(0, len(produtos)):
    if cont % 2 == 0:
        print(f'{cores['Produto']}{produtos[cont]:.<30}{cores['Limpar']}', end='')
    else:
        print(f'{cores['Valor']} R$ {produtos[cont]:>6.2f}{cores['Limpar']}')
print('=' * 40)
