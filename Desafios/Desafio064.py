"""
Desafio 064 - Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles.
(Desconsiderando a 'flag')
"""
num = 0
soma = 0
quant = 0
print('=' * 45)
print('{:^45}'.format('0 a 999'))
print('=' * 45)
print(' → Para encerrar o programa digite 999')
print('=' * 45)
while num < 999:
    num = int(input(' + Digite um valor: '))
    print('-' * 45)
    if num != 999:
        soma += num
        quant += 1
print(' Você digitou {} valore(s)'.format(quant))
print(' A soma entre esses valore(s) digitados é: {}'.format(soma))
print('=' * 45)
print('{:^45}'.format('FIM DO PROGRAMA'))
print('=' * 45)
