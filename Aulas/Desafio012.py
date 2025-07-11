# DESAFIO 012 - Faça um algoritimo que leia a o preço de um produto e mostre seu novo preço com 5% de desconto.
preco = float(input('Por favor digite o preço atual do produto: R$'))
desconto = preco * (5/100)
novopreco = preco - desconto
print('Com o desconto de 5% o novo preço do produto é R${}.'.format(novopreco))

