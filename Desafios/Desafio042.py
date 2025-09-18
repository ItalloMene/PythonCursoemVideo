"""
Desafio 042 - Refaça o Desafio035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais;
- Isósceles: dois lados iguais;
- Escaleno: todos os lados diferentes;
"""
reta1 = int(input('Digite o comprimento da primeira reta: '))
reta2 = int(input('Digite o comprimento da segunda reta: '))
reta3 = int(input('Digite o comprimento da terceira reta: '))
print(' ')
print('Reta 01: {} | Reta 02: {} | Reta 03: {}'.format(reta1, reta2, reta3))

if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print('Com essas retas \033[92mÉ POSSÍVEL\033[m formar um Triângulo.')
    if reta1 == reta2 == reta3:
        print('Sendo ele um \033[1;4mTriângulo Equilátero\033[m.')
    elif (reta1 == reta2) or (reta2 == reta3) or (reta1 == reta3):
        print('Sendo ele um \033[1;4mTriângulo Isósceles\033[m.')
    elif reta1 != reta2 != reta3 != reta1:
        print('Sendo ele um \033[1;4mTriângulo Escaleno\033[m.')
else:
    print('Com essas retas \033[91mNÃO É POSSÍVEL\033[m formar um Triângulo.')