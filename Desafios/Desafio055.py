"""
Desafio 055: Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
print('=' * 45)
print('{:^45}'.format('COMPARADOR DE PESOS'))
print('=' * 45)
maior_peso = 0
menor_peso = 0
for cont in range(1,6):
    peso = float(input('{}) Digite seu peso (Kg): '.format(cont)))
    print('-' * 45)
    if cont == 1:
        maior_peso = peso
        menor_peso = peso
        print('Primeiro peso registrado!')
        print('-' * 45)
    else:
        if peso > maior_peso:
            maior_peso = peso
            print('Maior peso atualizado!')
            print('-' * 45)
        if peso < menor_peso:
            menor_peso = peso
            print('Menor peso atualizado.')
            print('-' * 45)
print('{:^45}'.format('RESULTADO'))
print('-' * 45)
print('O MAIOR peso foi {:.1f}Kg'.format(maior_peso))
print('O MENOR peso foi {:.1f}Kg'.format(menor_peso))
print('=' * 45)

