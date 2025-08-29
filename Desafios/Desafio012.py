# DESAFIO 012 - Faça um algoritimo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto.
preco = float(input('Por favor digite o preço atual do produto: R$'))
desconto = preco * (5/100)
novopreco = preco - desconto
print('Com o desconto de \033[1;92m5%\033[m o novo preço do produto é: \033[1;4;92mR${:.2f}\033[m.'.format(novopreco))

