# DESAFIO 005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
numero = int(input('`Por favor, Digite um número: '))
antes = numero - 1
depois = numero + 1
print('O número digitado foi {}, seu sucessor é {} e seu antecessor é {}. '.format(numero, depois, antes))
