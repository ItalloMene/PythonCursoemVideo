"""
Desafio 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for cont in range (0, len(palavras)):
    print(f'{cont + 1}) Na palavra {palavras[cont].upper()} temos as vogais: ', end='')
    for letra in palavras[cont]:
        if letra in 'aeiou':
            print(f'{letra} ', end='')
    print('')
