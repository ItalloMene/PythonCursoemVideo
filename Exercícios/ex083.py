"""
Desafio 083: Crie um programa onde o usuário digite uma expressão (matemática) qualquer que use parênteses.
O seu aplicativo deverá analisar a se expressão está com os parênteses abertos e fechados na ordem correta.
"""
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')