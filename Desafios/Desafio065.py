"""
Desafio 065: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e
o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.
"""
print('=' * 45)
print('{:^45}'.format('MÉDIA, MAIOR, MENOR'))
print('=' * 45)

soma = 0
quant = 0
resp = 'S'
cont = 1

while resp == 'S':
    n = int(input('→ Digite um número: '))
    print('-' * 45)
    if cont == 1:
        maior = n
        menor = n
    else:
        if n >= maior:
            maior = n
        if n <= menor:
            menor = n
    resp = str(input('→ Continuar digitando [S/N]? ')).upper()
    print('-' * 45)
    soma += n
    quant += 1
    cont += 1

media = soma / quant
print(' → Média dos valores digitados: {:.1f}'.format(media))
print(' → Maior valor digitado: {}'.format(maior))
print(' → Menor valor digitado: {}'.format(menor))
print('=' * 45)
