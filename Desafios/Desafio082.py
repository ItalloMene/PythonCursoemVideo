"""
Desafio 082: Crie um programa que vai ler vários números e colocar numa lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente. Ao final mostre o conteúdo das três listas geradas.
"""
numeros = list()
pares = list()
impares = list()

print('=' * 50)
print(f'\033[96m{'LISTAS DE PARES E IMPARES':^50}\033[m')
print('=' * 50)

while True:
    num = int(input(' → Digite um número: '))
    print('-' * 50)
    numeros.append(num)

    while True:
        resposta = str(input(' → Deseja continuar (Sim/Não)? ')).strip().upper()[0]
        print('-' * 50)
        if resposta in 'SsNn':
            break

    if resposta in 'Nn':
        break

for valor in numeros:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print('=' * 50)
print(f'\033[96m{'RESULTADOS':^50}\033[m')
print('=' * 50)

print(f' → Lista completa: \033[93m{numeros}\033[m')
print(f' → Lista de valores pares: \033[94m{pares}\033[m')
print(f' → Lista de valores impares: \033[95m{impares}\033[m')
print('=' * 50)
