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
print(f'\033[94m{"INTEIRO E REAL":^50}\033[m')
linha()
i = r = 0
while True:
    ok1 = False
    try:
        i = leiaInt('→ Digite um número inteiro: ')
    except Exception as erro:
        print(f'\033[31mERRO: por favor, digite um número inteiro válido!\033[m')
    except KeyboardInterrupt:
        print('\n\033[93m usuário preferiu não informar o valor.\033[m')
        break
    else:
        while True:
            ok2 = False
            try:
                r = leiaFloat('→ Digite um número real: ')
            except Exception as erro:
                print(f'\033[31mERRO: por favor, digite um número real válido!\033[m')
            except KeyboardInterrupt:
                print(f'\n\033[93mO usuário preferiu não informar o valor.\033[m')
                break
            else:
                ok2 = True
            if ok2:
                break
        ok1 = True
    if ok1:
        break
linha()
print(f'→ O valor inteiro digitado foi \033[96m{i}\033[m e o real foi \033[96m{r:.1f}\033[m')
print('→ Fim do programa! Volte sempre!')
linha()
