# DESAFIO 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Por favor, digite um valor em metros (x.xx): '))
centimetros =  metros * 100
milimetros = metros * 1000
print('O valor digitado foi {}m, sendo {}cm (centímetros) e {}mm (milímetros). '.format(metros, centimetros, milimetros))