# DESAFIO 011 - Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-lá
# Sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('Por favor, Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = altura * largura
tinta = area / 2
print('Para pintar a árede com área de {}m² será necssário {}L de tinta'.format(area, tinta))


