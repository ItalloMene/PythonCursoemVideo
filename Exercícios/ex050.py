"""
Desafio 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor digitado for impar, desconsidere-o.
"""
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num # Mesmo que: soma = soma + num | Acumulador
        cont += 1 # Mesmo que: cont = cont + 1 | Contador
print('Você informou {} números PARES e a soma foi {}.'.format(cont, soma))
