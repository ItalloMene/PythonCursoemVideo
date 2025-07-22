# DESAFIO 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Por favor, digite o ângulo: '))
radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)
print('Segundo o Valor {} do ângulo, seu radiano é {:.4f}, o seno é {:.4f}, o cosseno é {:.4f} e a tangente é {:.4f}.'.format(angulo, radiano, seno, cosseno, tangente))
