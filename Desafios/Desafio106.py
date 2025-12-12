"""
Desafio 106: Faça um Mini-sistema que utilize o InteractiveHelp do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM',
o programa se encerrará.
OBS: use cores.
"""
cores = {
    'azul':'\033[1;94m',
    'verde':'\033[1;92m',
    'ciano':'\033[1;96m',
    'branco':'\033[1;97m',
    'limpar':'\033[m'
}

from time import sleep

def linha():
    print(f'{cores['ciano']}=' * 100)

def cabeçalho(txt):
    linha()
    print(f'{cores['azul']}{txt:^100}')
    linha()

def ajuda(msg):
    sleep(1)
    print(f'{cores["branco"]}{" ":<30}Acessando o manual do comando "{msg}"...')
    linha()
    print(f'{cores['verde']}')
    sleep(1)
    help(msg)


# Programa Principal
cabeçalho("Sistema de Ajuda PyHelp")

while True:
    sleep(1)
    print(f'{cores['azul']} → Digite "FIM" para finalizar.')
    sleep(1)
    resposta = str(input(' → Digite a função ou biblioteca: ')).strip()
    linha()
    if resposta in 'FIMfim':
        sleep(1)
        print(f'{cores['branco']}{" ":<30}Fim do programa! Volte sempre!')
        linha()
        break
    ajuda(resposta)
    linha()
