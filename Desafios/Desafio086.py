"""
Desafio 086: Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = list()
colunas = list()
linhas = list()

print('=' * 40)
print(f'{"MONTANDO MATRIZ 3X3":^40}')
print('=' * 40)

for linha in range(0, 3):
    linhas.clear()
    for coluna in range(0, 3):
        num = int(input(f' → Digite um valor para [{linha},{coluna}]: '))
        colunas.append(num)
        linhas.append(colunas[:])
        colunas.clear()
    matriz.append(linhas[:])

print('=' * 40)
for linha in range(0, 3):
    for coluna in range(0,3):
       print(f'{"":^7}{matriz[linha][coluna]}', end='')
    print()
print('=' * 40)
