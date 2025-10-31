"""
Desafio 081: Crie um programa que vai ler vários números e colocar numa lista.
Depois disso, mostre:
A) Quantos números foram digitados
B) A lista de valores, ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista
"""
texto = {
    'negativo' : '\033[1;91m',
    'positivo' : '\033[1;92m',
    'titulo' : '\033[1;94m',
    'atencao1' : '\033[1;93m',
    'atencao2' : '\033[1;95m',
    'limpar' : '\033[m'
}

print('=' * 50)
print(f'{texto['titulo']}{'ANALISADOR DE LISTA':^50}{texto['limpar']}')
print('=' * 50)

numeros = list()

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

print('=' * 50)
print(f'{texto['titulo']}{'RESULTADOS':^50}{texto['limpar']}')
print('=' * 50)

print(f' A) Foram digitados {texto['atencao1']}{len(numeros)}{texto['limpar']} números na lista.')

numeros.sort(reverse=True)
print(f' B) lista ordenada de forma decrescente: {texto['atencao2']}{numeros}{texto['limpar']}')

if 5 in numeros:
    print(f' {texto['positivo']}C) O valor 5 foi digitado e está na lista.{texto['limpar']}.')
else:
    print(f' {texto['negativo']}C) O valor 5 NÃO foi digitado nem está na lista.{texto['limpar']}')
print('=' * 50)
