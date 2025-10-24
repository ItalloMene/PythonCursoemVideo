"""
Desafio 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final mostre:
A) Quantas vezes aparece o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares
"""
print('=' * 40)
print(f'{'LISTAGEM DE NÚMEROS':^40}')
print('=' * 40)
for cont in range (1,5):
    num = int(input(f' {cont} - Digite um número: '))
    if cont == 1:
        n1 = num
    elif cont == 2:
        n2 = num
    elif cont == 3:
        n3 = num
    elif cont == 4:
        n4 = num
numeros = (n1, n2, n3, n4)

print('-' * 40)
print(f'{'RESULTADOS':^40}')
print('-' * 40)
print(f' → Lista gerada: {numeros}.')
print(f' → O número 9 aparece {numeros.count(9)} vezes.')

if not 3 in numeros:
    print(f' → O número 3 não está nessa lista.')
else:
    print(f' → O número 3 aparece na posição {numeros.index(3) + 1}.')

print(f' → Os números pares foram:', end=' ')
for cont in range (0, len(numeros)):
    if numeros[cont] % 2 == 0:
        print(f'{numeros[cont]}', end=' ')
    else:
        print('--', end=' ')
print('\n','=' * 40)