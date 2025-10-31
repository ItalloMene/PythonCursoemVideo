"""
Desafio 078: Faça um programa que leia 5 valores numéricos e guarde os numa lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
numeros = list()

print('=' * 50)
for contador in range(1, 6):
    numero = int(input(f'→ Digite o {contador}º número para lista: '))
    numeros.append(numero)

print('-' * 50)
print(f'→ Lista formada: {numeros}')

maior = menor = numeros[0]

for contador in range(0, len(numeros)):
    if numeros[contador] > maior:
        maior = numeros[contador]
    if numeros[contador] < menor:
        menor = numeros[contador]

posicoes_maior = list()
posicoes_menor = list()

for posicao, valor in enumerate(numeros):
    if valor == maior:
        posicoes_maior.append(posicao + 1)
    if valor == menor:
        posicoes_menor.append(posicao + 1)

print(f'→ Maior número encontrado: {maior} | Nas posições: {posicoes_maior}')
print(f'→ Menor número encontrado: {menor} | Nas posições: {posicoes_menor}')
print('=' * 50)

