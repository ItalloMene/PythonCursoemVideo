"""
cont = 1
while cont <= 10:
    print(cont, '→', end=' ')
    cont += 1
print('Acabou')0
"""
"""
cont = 1
while True:
    print(cont, '→', end='')
    cont +=1
print('Acabou')
"""
"""
# Repetição 'Enquanto' utilizando flags
n = 0
while n != 1000:
    n = int(input('Digite um número: '))
"""
"""
n = cont = 0
while cont < 5:
    n = int(input('Digite um número: '))
    cont += 1
"""
"""
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999 # Gambiarra
print('A soma vale {}'.format(s))
"""
"""
# Uso do BREAK no LOOPING INFINITO
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}.') # Uso da f-strings
"""
# Exemplo de uso da f-string, entre outros:
nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos.') # PYTHON 3.6+
print('O {} tem {} anos.'.format(nome, idade)) # PYTHON 3
print('O %s tem %d anos.' % (nome, idade)) # PYTHON 2
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')
print(f'| \033[1;97;41m {nome:<20} \033[m | \033[1;97;44m {idade:^20}  \033[m | \033[1;97;43m {salario:>20} \033[m |')