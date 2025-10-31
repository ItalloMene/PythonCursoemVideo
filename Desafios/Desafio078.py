"""
Desafio 078: Faça um programa que leia 5 valores numéricos e guarde os numa lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
numeros = list()
for contador in range(1, 6):
    numero = int(input(f'→ Digite o {contador}º número para lista: '))
    numeros.append(numero)
print('-' * 45)
for contador in range(0, len(numeros)):
    if contador == 0:
        maior = menor = numeros[0]
        posiçãomaior = posiçãomenor = numeros.index(numeros[0])
    else:
        if maior >= numeros[contador]:
            maior = numeros[contador]
            posiçãomaior = numeros.index(numeros[contador])
        if menor <= numeros[contador]:
            menor = numeros[contador]
            posiçãomenor = numeros.index(numeros[contador])
print(f'→ Lista formada: {numeros}')
print(f'→ Maior número encontrado: {maior} | Na posição: {posiçãomaior + 1}')
print(f'→ Menor número encontrado: {menor} | Na posição: {posiçãomenor + 1}')
