"""
Desafio 042 - Refaça o Desafio035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais;
- Isósceles: dois lados iguais;
- Escaleno: todos os lados diferentes;
"""
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo.', end='')
    if r1  == r2 and r2 == r3: # if r1 == r2 == r3:
        print(' EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print(' ESCALENO!')
    else:
        print(' ISÓCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')

