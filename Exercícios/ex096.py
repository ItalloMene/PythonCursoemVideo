"""
Desafio 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retângular
(largura e comprimento) e mostre a área do terreno.
"""
def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')


#Programa principal
print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
