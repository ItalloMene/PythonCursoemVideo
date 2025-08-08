'''
DESAFIO 026 - Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A";
- Em que posição ela aparece a primeira vez;
- Em que posição ela aparece pela ultima vez;
'''
frase = str(input('Por favor, digite uma frase: '))
aparece = frase.upper().count('A')
primeiro = frase.upper().find('A')
ultimo = frase.upper().rfind('A')
print('A letra "A" aparece {} vezes na frase digitada;'.format(aparece))
print('A letra "A" aparece pela primeira vez na posição {};'.format(primeiro))
print('A letra "A" aparece pela ultima vez na posição {};'.format(ultimo))
