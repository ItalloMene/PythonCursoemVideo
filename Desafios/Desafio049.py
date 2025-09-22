"""
Desafio 049: Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
"""
from time import sleep
print('=' * 35)
print('{:^35}'.format('TABUADA'))
print('=' * 35)
numero = int(input(' > Por favor escolha um número: '))
print('=' * 35)
print('{:^35}'.format('RESULTADO'))
print('=' * 35)
for contador in range(0, 11):
    print('{:^12}{} x {:2} = {}'.format(' ',numero, contador, numero * contador))
    sleep(1)
print('=' * 35)
print('{:^35}'.format('FIM'))
print('=' * 35)