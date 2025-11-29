"""
Desafio 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável.
Ex: escreva('Olá, Mundo!')
saída:
~~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~~
"""
def escreva(frase):
    print('~' * len(frase))
    print(f'{frase}')
    print('~' * len(frase))

texto = str(input('Digite sua frase: '))
escreva(texto)