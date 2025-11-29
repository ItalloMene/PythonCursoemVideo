"""
Desafio 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retângular
(largura e comprimento) e mostre a área do terreno.
"""
def area(l, c):
    terreno = l * c
    print(f'→ A área do terreno é: {terreno:.1f}m²')
def linha():
    print('=' * 35)


linha()
print(f'{"CALCULO ÁREA TERRENO":^35}')
linha()
largura = float(input('→ Digite a largura da área: '))
comprimento = float(input('→ Digite o comprimento da área: '))
linha()
area(l = largura, c = comprimento)
linha()
