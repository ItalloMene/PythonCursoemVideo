# DESAFIO 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1,00 = R$3,27
# Valores atuais: Dólar = 5,59 Euro = 6,52 Iene = 0,038 (julho, 2025)

cores = {
    'Real' : '\033[1;32m',
    'Dollar' : '\033[1;37m',
    'Euro' : '\033[1;34m',
    'Ienes' : '\033[1;31m',
    'Limpar' : '\033[m'
}



real = float(input('Por favor, digite qual valor em Real você possui na carteira (xx.xx): R$'))
dollar = real / 5.59
euro = real / 6.52
iene = real / 0.038
print('Com {}{:.2f} Reais{} você pode comprar {}{:.2f} Dollars{}, ou {}{:.2f} Euros{}, ou {}{:.2f} Ienes{}'.format(cores['Real'], real, cores['Limpar'], cores['Dollar'], dollar, cores['Limpar'], cores['Euro'], euro, cores['Limpar'], cores['Ienes'], iene, cores['Limpar']))
