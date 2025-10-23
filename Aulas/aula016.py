"""
lanche = 'Hamburguer'
print(lanche)
lanche = 'Suco'
print(lanche)
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
# ou
lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'

# Manipulação de Tupla
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])

# Tuplas são imutáveis
lanche [1] = 'Refrigerante'
# Este comando apresentará erro, as tuplas podem ser alteradas apenas na sua declaração

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('-' * 40)

for cont in range(0, len(lanche)):
    print(cont)
print('-' * 40)

# Mostrando o Dado e a Posição
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} | Posição: {cont}')
print('-' * 40)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} | Posição {pos}')


# Mostrar a tupla de forma organizada:
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche))
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(a)
print(b)
print(c)
print(d)
print(len(c))
# quantas vezes o número 5 aparece na Tupla "c"
print(c.count(5))
print(c.count(4))
print(c.count(9))
# em qual posição está o 8
print(c.index(8))
print(c.index(4))
print(d.index(5))
print(d.index(5, 1)) # verifica a partir da posição 1

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
del(pessoa)
print(pessoa)

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa[0])
"""