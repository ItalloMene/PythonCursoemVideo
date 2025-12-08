"""
Desafio 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO
nas eleições.
"""
from datetime import date

def voto(ano):
    """
    → Faz uma análise da idade do usuário para mostrar se o seu voto é Opcional, Obrigatório ou Negado.
    :param ano: Recebe o ano de nascimento do usuário
    :return: sem retorno
    """

    idade = date.today().year - ano
    if idade < 16:
        print(f'→ Sendo sua idade \033[4m{idade}\033[m anos seu voto foi \033[91mNEGADO.\033[m')
    elif (idade >= 18) and (idade <= 70):
        print(f'→ Sendo sua idade \033[4m{idade}\033[m anos seu voto é \033[92mOBRIGATÓRIO.\033[m')
    else:
        print(f'→ Sendo sua idade \033[4m{idade}\033[m anos seu voto é \033[93mOPCIONAL.\033[m')


# Programa principal:
print('=' * 50)
nasc = int(input('→ Digite seu ano de nascimento: '))
print('-' * 50)
voto(nasc)
print('=' * 50)
#help(voto)