"""
Desafio 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input()
do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um número')
"""
def linha():
    print('=' * 45)

def leiaInt(msg):
    val = ''
    while not val.isnumeric():
        print(msg, end='')
        val = input()
        if not val.isnumeric():
            print('\033[1;91m → ERRO! Digite um número inteiro válido.\033[m')
            linha()
    return val


# Programa principal
linha()
n = leiaInt(' → Digite um número: ')
print(f' → Você acabou de digitar o número \033[94m{n}\033[m.')
linha()