"""
Desafio 086: Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = list()
linhas = list()

print('=' * 40)
print(f'{"MONTANDO MATRIZ 3X3":^40}')
print('=' * 40)

for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f' → Digite um valor para [{linha},{coluna}]: '))
        linhas.append(num)
    matriz.append(linhas[:])
    linhas.clear()

print('=' * 40)
for linha in range(0, 3):
    for coluna in range(0,3):
       print(f' [{matriz[linha][coluna]:^10}]', end='')
    print()
print('=' * 40)
