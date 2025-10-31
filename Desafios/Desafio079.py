"""
Desafio 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os numa lista,
caso o número já exista la dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente.
"""
print('=' * 50)
print(f'{'CRIE SUA LISTA NUMÉRICA':^50}')
print('=' * 50)

numeros = list() # Criação da lista números

while True: # Looping adição de números a Lista
    numero = int(input(' → Digite um número: ')) # recebe o valor
    if numero in numeros: # Se o valor já estiver na lista
        print(f' → Número não foi adicionado por já estar na lista.')
    else: # Se não estiver na lista
        numeros.append(numero)
        print(f' → Número adicionado a lista com sucesso')
    print('-' * 50)

    while True: # looping para que o programa apenas prossiga se a resposta igualar a Sim ou Não
        resposta = str(input(' → Deseja continuar (Sim / Não)? ')).strip().upper()[0]
        print('-' * 50)
        if resposta in 'SsNn':
            break

    if resposta == 'N': # Quebra do looping Adição de Números a Lista
        break

numeros.sort() # ordena de forma crescente os números da Lista
print(f' → A lista criada ordenada é: {numeros}')
print('-' * 50)
