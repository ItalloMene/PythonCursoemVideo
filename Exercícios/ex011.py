# DESAFIO 011 - Faça um programa que leia a largura e a altura de uma parede em
# metros, calcule a sua área e a quantidade de tinta necessária para pintá-la.
# Sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input('Largura de parede: '))
alt = float(input('Altura de parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, voc~e precisará de {}L de tinta'.format(tinta))