# DESAFIO 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Por favor, digite um valor em metros (x.xx): '))
centimetros =  metros * 100
milimetros = metros * 1000
print('\033[1;4;41m O valor digitado foi: \033[1;4;42m {}m \033[1;41m, sendo \033[1;4;46m {}cm \033[1;41m (centímetros)  e \033[1;4;43m {}mm \033[1;41m (milímetros).\033[m'.format(metros, centimetros, milimetros))