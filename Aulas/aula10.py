"""
# Estrutura Condicional Simples:
nome = str(input('Qual é o seu nome? '))
if nome == 'Itallo':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))

# Estrutura Condicional Composta:
nome = str(input('Qual é o seu nome? '))
if nome == 'Itallo':1
2

    print('Que nome lindo você tem!')
else:
    print('O seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
"""

# Exemplo de CONDIÇÃO COMPOSTA para avaliar a média do aluno:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! ')
else:
    print('Sua média foi ruim! ')
# CONDIÇÃO SIMPLIFICADA para avaliar a média do aluno:
print('PARABÉNS!' if m >= 6.0 else 'ESTUDE MAIS!')