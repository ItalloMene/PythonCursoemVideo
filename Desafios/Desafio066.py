"""
Desafio 066: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar valor 999, que é a condição de parada.
No final mostre quantos números foram digitados e qual foi a soma entre eles.
(desconsiderando a 'flag')
"""
cores = {
    'azul' : '\033[1;94m',
    'ciano' : '\033[96m',
    'limpar' : '\033[m'
}

print('=' * 35)
print(f'{cores['ciano']}{'QUANTIDADE E SOMA':^35}{cores['limpar']}')
print('=' * 35)

print(' DIGITE 999 PARA PARAR O PROGRAMA')
print('-' * 35)

soma = quant = 0
while True:
    numero = int(input(' → Digite um número: '))
    if numero == 999:
        break
    soma += numero
    quant += 1

print('-' * 35)
print(f' - Você digitou {cores['azul']}{quant}{cores['limpar']} valores. \n - E a soma entre eles é {cores['azul']}{soma}{cores['limpar']}.')
print('=' * 35)
