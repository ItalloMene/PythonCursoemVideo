# DESAFIO 4 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

val = input('Por favor, digite algo:')
print(type(val))
print('tem apenas letras?', val.isalpha())
print('tem apenas números?', val.isnumeric())
print('tem letras e/ou números?', val.isalnum())
print('tem apenas letras maiúsculas?', val.isupper())
print('tem apenas letras minúsculas?', val.islower())
