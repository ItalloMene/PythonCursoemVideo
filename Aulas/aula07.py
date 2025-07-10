# OPERADORES
print('EXEMPLO OPERADORES:')
print('5 + 2 ==', 5 + 2)
print('5 - 2 ==', 5 - 2)
print('5 * 2 ==', 5 * 2)
print('5 / 2 ==', 5 / 2)
print('5 ** 2 ==', 5 ** 2)
print('5 // 2 ==', 5 // 2)
print('5 % 2 ==', 5 % 2)

print(' ')

# ORDEM DE PRECEDÊNCIA
# 1 (), 2 **, 3 * / // %, 4 + -
print('EXEMPLO ORDEM DE PRECEDÊNCIA: ')
print('5 + 3 * 2 == ', 5 + 3 * 2)
print('3 * 5 + 4 ** 2 ==', 3 * 5 + 4 ** 2)
print('3 * (5 + 4) ** 2 == ', 3 * (5 + 4) ** 2)

# FORMATAÇÃO PRINT
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))