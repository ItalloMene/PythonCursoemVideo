"""
Desafio 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os numa lista,
(sem usar o sort). No final, mostre a lista ordenada na tela.
"""
numeros = list()

for cont in range (1, 6):
    numeros.append(int(input(f' {cont}) Digite um número: ')))

for passo in range(len(numeros) - 1):
    for comparador in range(len(numeros) - 1 - passo):
        if numeros[comparador] > numeros[comparador + 1]:
            numeros[comparador], numeros[comparador + 1] = numeros[comparador + 1], numeros[comparador]

print('-' * 40)
print(f'> A lista ordenada sem o uso do sort() é: {numeros}')