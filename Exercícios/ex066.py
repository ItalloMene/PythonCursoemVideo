"""
Desafio 066: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar valor 999, que é a condição de parada.
No final mostre quantos números foram digitados e qual foi a soma entre eles.
(desconsiderando a 'flag')
"""

"""
# Resposta 01: Com gambiarra
num = soma = 0
while num != 999:
    num = int(input('Digite um valor (999 para parar): '))
    soma += num
soma -= 999
print(f'A soma dos valores foi {soma}!')
"""

# Resposta 02: Utilizando Looping infinito com break
soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')