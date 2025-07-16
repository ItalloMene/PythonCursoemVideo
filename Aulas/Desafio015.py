# DESAFIO 015 - Esacreva um programa que pergunte a quantidade de Km
# percorrido por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar.
# Sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Km foram percorridos? '))
dia = int(input('Por quantos dias o veículo foi utilizado? '))
valkm = km * 0.15
valdia = dia * 60
conta = valdia + valkm
print('O total a pagar por {:.0f}Km percorridos e {} dias alugados é de R${:.2f}'.format(km, dia, conta))