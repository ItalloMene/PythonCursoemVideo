"""
Desafio 087: Aprimore o Desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna
C) O maior valor da segunda coluna
"""
print('=' * 50)
print(f'\033[1;93m{"MATRIZ 3x3 2.0":^50}\033[m')
print('=' * 50)

matriz = list()
linhas = list()

for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f' → Digite um valor para [{linha}, {coluna}]: '))
        linhas.append(valor)
    matriz.append(linhas[:])
    linhas.clear()
print('=' * 50)

soma_par = soma_terceira = maior_valor = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'  \033[1;93m[{matriz[linha][coluna]:^10}]\033[m', end='')

        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
    print()

    if matriz[linha][2]:
        soma_terceira += matriz[linha][2]

    if matriz[linha][1] > maior_valor:
        maior_valor = matriz[linha][1]

print('=' * 50)
print(f'\033[1;94m{"RESULTADOS":^50}\033[m')
print('=' * 50)

print(f'A) Soma de todos os valores PARES digitados = \033[1;4;94m{soma_par}\033[m')
print(f'B) Soma de todos os valores da TERCEIRA COLUNA = \033[1;4;94m{soma_terceira}\033[m')
print(f'C) Maior valor da SEGUNDA COLUNA = \033[1;4;94m{maior_valor}\033[m')
print('=' * 50)


