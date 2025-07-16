# DESAFIO 0I14 - Escreva um programa que leia uma temperatura digitada em °C e converta para °F.
c = float(input('Iforme a temperatura em °C: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))