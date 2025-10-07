"""
Desafio 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""
print('=' * 100)
print('{}{:^100}{}'.format('\033[93m','FATORIAL','\033[m'))
print('=' * 100)

num = int(input(' → Digite um número: '))

if num <= 0:
    print(' Tente novamente!\n Valores acima de Zero!')
else:
    multi = num - 1
    cont = num
    print(' {}! = {}'.format(num, num), end='')
    while multi > 0:
        print(' x {}'.format(multi),end='')
        fatorial = num * multi
        num = fatorial
        multi -= 1
        cont -= 1
    print(' = {}'.format(fatorial))