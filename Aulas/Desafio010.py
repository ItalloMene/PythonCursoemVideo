# DESAFIO 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1,00 = R$ 3,27
# Valores atuais: Dólar = 5.59 Euro = 6.52 Iene = 0,038 (Julho, 2025)

real = float(input('Por favor, digite qual valor em Real você possui na carteira (xx.xx): R$'))
dolar = real / 5.59
euro = real / 6.52
iene = real / 0.038
print('Com {:.2f} Reais você pode comprar {:.2f} Dolares, ou {:.2f} Euros, ou {:.2f} Ienes '.format(real, dolar, euro, iene))
