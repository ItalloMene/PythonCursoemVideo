# apresentará erro já que Tuplas são imutáveis
"""
num = (2, 5, 9, 1)
num[2] = 3
print(num)
"""
# Está versão funcionará por se tratar de uma lista que pode ser modificada
num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
# num[4] = 7 # não funciona, pois a adição de elemento não é feito dessa forma na lista
num.append(7) # assim pode-se adicionar um elemento a lista
print(num)
num.sort() # Ordena a lista
print(num)
num.sort(reverse=True) # Ordena a lista de forma reversa
print(num)
print(f'Essa lista tem {len(num)} elementos.') # len() mostra quantos elementos tem na lista
num.insert(2, 0) # insere o valor zero na posição dois
print(num)
num.pop() # elimina o ultimo valor da lista
print(num)
num.pop(2) # elimina o elemento na posição dois
print(num)
num.insert(2, 2)
print(num)
num.remove(2) # elimina o primeiro elemento com o valor dois que encontrar na lista
print(num)
if 4 in num: # se houver 4 na lista num
    num.remove(4) # remova o elemento com valor quatro
else: # se não
    print('Não achei o número 4') # mostre a mensagem...
if 5 in num: # se tiver o valor 5 na lista remover ele
    num.remove(5)
    print(num)
else: # se não mostrar a mensagem
    print('Não achei o número 5')
valores = list() # mesmo que valores = [] | criação da lista vazia
valores.append(5) # adição do elemento 5 a lista valores
valores.append(9)
valores.append(4)
for v in valores: # para cada valor em valores
    print(f'{v}...', end='')
print('')
for c, v in enumerate(valores): # mostrar a chave(índice) e o valor com auxilio do enumerate() para contar os dois
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
numeros = list()
for cont in range(0, 5): # Lista sendo formada com números digitados pelo usuário
    numeros.append(int(input('Digite um valor: ')))
for c, v in enumerate(numeros): # leitura do valor digitado pelo usuário e a sua respectiva posição na lista criada
    print(f'Na posição {c} encontrei o valor {v}!')
a = [2, 3, 4, 7]
b = a # ligação de uma lista com a outra Lista B ligada a Lista A
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b[2] = 8 # Por estarem ligadas, ambas as listas, tem os seus valores na posição 2 mudados para o valor 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
c = [2, 3, 4, 7]
d = c[:] # D recebe uma cópia de todos os elementos da lista C
print(f'Lista C: {c}')
print(f'Lista D: {d}')
d[2] = 8
print(f'Lista C: {c}')
print(f'Lista D: {d}') # apenas a lista D troca o valor que está na posição 2 pelo valor 8

