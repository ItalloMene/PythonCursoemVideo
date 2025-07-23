# DESAFIO 0I14 - Escreva um programa que leia uma temperatura digitada em °C e converta para °F.
C = float(input('Digite uma temperatura em °C: '))
F = (C * 1.8) + 32
print('{:.1f}°C é igual a {:.1f}°F'.format(C, F))