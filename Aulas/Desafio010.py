# DESAFIO 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1,00 = R$ 3,27

real = float(input('Por favor, digite qual valor em Real você possui na carteira (xx.xx): R$'))
dolar = real / 3.27
print('Com R${:.3} você pode comprar US${:.3}'.format(real, dolar))