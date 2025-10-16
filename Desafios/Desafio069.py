"""
Desafio 069: crie um programa que leia a idade e o sexo de várias pessoas.
Cada pessoa cadastrada, o programa deverá perguntar se o usuário deseja continuar.
No final mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
"""
print('=' * 60)
print(f'\033[1;33m{'CADASTRE-SE':^60}\033[m')
print('=' * 60)
mais18 = homens = mulherMenos20 = 0
while True:
    nome = str(input(' → Digite seu nome: '))
    idade = int(input(' → Digite sua idade: '))
    # Contador quantidade de pessoas maiores de 18
    if idade > 18:
        mais18 += 1
    # Looping para quando a resposta for M ou F
    while True:
        sexo = str(input(' → Digite seu sexo (Masculino / Feminino): ')).upper().strip()[0]
        if sexo in 'MmFf':
            break
    # Contador quantidade de Homens
    if sexo in 'Mm':
        homens += 1
    # Contador quantidade de Mulheres com menos de 20 anos
    if (sexo in 'Ff') and (idade < 20):
        mulherMenos20 += 1
    # Looping para quando a resposta for S ou N
    while True:
        continuar = str(input(' → Deseja continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'SsNn':
            break
    print('-' * 60)
    # Parada do programa quando a resposta do continuar dor N
    if continuar == 'N':
        break
print(f'\033[1;32m{'RESULTADOS':^60}\033[m')
print('-' * 60)
print(f' → {mais18} pessoas tem mais de 18 anos.')
print(f' → {homens} homens foram cadastrados.')
print(f' → {mulherMenos20} mulheres com menos de 20 anos foram cadastradas.')
print('=' * 60)
