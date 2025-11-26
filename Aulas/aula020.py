"""
def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print('-' * 30)

# Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(a=4, b=5)
soma(b=3, a=7)
"""

"""
def contador1(* núm):
    for valor in núm:
        print(valor, end='')
    print('Fim')
    print('-' * 20)
def contador2( * núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')


# Programa principal
contador1(2, 1, 7)
contador1(8, 0)
contador1(4, 4, 7, 6, 2)
contador2(2, 1, 7)
contador2(8, 0)
contador2(4, 4, 7, 6, 2)
"""

"""
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


#Programa principal
valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)
"""

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


# Programa principal
soma(5, 2)
soma(2, 9, 4)
