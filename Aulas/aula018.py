"""
# Exemplo 01:
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
print(teste)
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(teste)
print(galera)
"""
"""
# Exemplo 02: Cópia de lista
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print(teste)
"""
"""
# Exemplo 03: Estrutura lista composta
galera = [['João', 39], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
print(galera[3][0])
print(galera[2])
print('-' * 20)
for p in galera:
    print(p)
print('-' * 20)
for p in galera:
    print(p[0])
print('-' * 20)
for p in galera:
    print(p[1])
print('-' * 30)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
print('-' * 30)
"""
# Exemplo 04: coleta de dado
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # Adiciona uma cópia da lista dado a lista galera
    dado.clear() # Limpa a lista dado
print(galera)
# Obs com o clear se o comando galera.append(dado) sem os símbolos [:] for usado o print(galera) mostrará uma lista vazia
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
