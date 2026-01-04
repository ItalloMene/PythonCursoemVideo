"""
Desafio 113: Reescreva a função leiaInt() que fizemos no Desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com mesma funcionalidade.
"""
def linha():
    print('=' * 50)


def leiaInt(msg):
    i = int(input(msg))
    return i


def leiaFloat(msg):
    r = float(input(msg))
    return r


# Programa Principal
linha()
print(f'\033[93m{"INTEIRO E REAL":^50}\033[m')
linha()

while True:
    ok = False

    try:
        i = leiaInt('→ Digite um número inteiro: ')
    except Exception as erro:
        print(f'\033[31mERRO: por favor, digite um número inteiro válido!\033[m')
    else:
        ok = True

    if ok:
        break

while True:
    ok = False

    try:
        r = leiaFloat('→ Digite um número real: ')
    except Exception as erro:
        print(f'\033[31mERRO: por favor, digite um número real válido!\033[m')
    else:
        linha()
        print(f'→ O valor inteiro digitado foi \033[96m{i}\033[m e o real foi \033[96m{r:.1f}\033[m')
        print('→ Fim do programa! Volte sempre!')
        ok = True

    if ok:
        break
linha()
