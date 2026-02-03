def linha():
    print('=' * 40)


def cabeçalho(msg):
    linha()
    print(f'{msg.center(40)}')
    linha()


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('\nUsuário preferiu nãi digitar esse número.')
            return 0
        else:
            return n


def Menu(lista):
    cabeçalho('MENU CADASTRO')
    pos = 1
    for item in lista:
        print(f'{pos} - {item}')
        pos += 1
    linha()
    opção = leiaInt('Sua Opção: ')
    return opção