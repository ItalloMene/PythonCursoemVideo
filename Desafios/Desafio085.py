"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os numa lista única que mantenha
separados os valores pares e os valores ímpares. No final mostre os valores pares e ímpares em ordem crescente.
"""
print('=' * 50)
print(f'\033[93m{"LISTAS: PARES E ÍMPARES":^50}\033[m')
print('=' * 50)

numeros = list()
pares = list()
impares = list()

for cont in range(1, 8):
    num = (int(input(f'{" ":^13}Digite o {cont}º valor: ')))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

pares.sort()
impares.sort()
numeros.append(pares[:])
numeros.append(impares[:])

print('-' * 50)
print(f' Os valores \033[1mPARES\033[m digitados são: \033[96m{numeros[0]}\033[m')
print(f' Os valores \033[1mÍMPARES\033[m digitados são: \033[96m{numeros[1]}\033[m')
print('=' * 50)
