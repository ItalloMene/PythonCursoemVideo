# EXEMPLO 01: repetir apenas a string "Oi"
for c in range (0, 6):
    print('Oi')
print('FIM')
print('=' * 20)

# EXEMPLO 02: repetir as strings "oi" e "fim"
for c in range (0,6):
    print('oi')
    print('fim')
print('=' * 20)

# EXEMPLO 03: Contagem 6 vezes.
for c in range (0,6):
    print(c)
print('FIM')
print('=' * 20)

# EXEMPLO 04: Contagem 5 vezes.
for c in range (1, 6):
    print(c)
print('FIM')
print('=' * 20)

# EXEMPLO 05: Contagem de trás para frente
for c in range (6, 0, -1):
    print(c)
print('FIM')
print('=' * 20)

# EXEMPLO 06: Contagem pulando a cada dois números.
for c in range (0, 7, 2):
    print(c)
print('FIM')
print('=' * 20)

# EXEMPLO 07: Contagem por número escolhido
n = int(input('Digite um número: '))
for c in range (0, n):
    print(c)
print('FIM')
print('=' * 20)
# EXEMPLO 08: Contagem até o número escolhido:
n = int(input('Digite um número: '))
for c in range (0, n+1):
    print(c)
print('FIM')
print('=' * 20)

# EXEMPLO 09: Inicio, Fim, Passo escolhidos pelo usuário
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
print('=' * 20)

# EXEMPLO 10: Repetição do “Input” / Ler o valor 3 vezes
for c in range(0,3):
    n = int(input('Digite um valor: '))
print('FIM')
print('=' * 20)

# EXEMPLO 11: Somatório de todos os valores digitados
s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}.'.format(s))