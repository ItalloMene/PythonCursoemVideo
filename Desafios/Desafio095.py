"""
Desafio 095: Aprimore o Desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
de detalhes ao aproveitamento do jogador.
"""
jogadores = []

print('=' * 50)
print(f"{'GERENCIADORE DE APROVEITAMENTO JOGADORES':^50}")
print('=' * 50)
while True:
    gols = []
    tot_gols = 0

    nome = str(input(' → Digite o nome do jogador: '))
    partidas = int(input(f' → Digite quantas partidas {nome} jogou: '))

    for partida in range (1, partidas + 1):
        gols.append(int(input(f' → Quantas gols {nome} fez na {partida}º partida? ')))

    for valor in gols:
        tot_gols += valor
    jogador = {'nome':nome, 'gols':gols[:], 'total':tot_gols}
    jogadores.append(jogador.copy())

    while True:
        resposta = str(input(' → Deseja continuar [S/N]? ')).strip().upper()[0]
        if resposta in 'SN':
            break
    print('-' * 50)

    if resposta in 'N':
        break

print(f' {"Cód":<5} {"Nome":<12} {"Gols":<20} {"Total":>5}')
print('=' * 50)

cont = 0
for item in jogadores:
    print(f" {cont:<5} {item['nome']:<12} {str(item['gols']):<20} {item['total']:>5}")
    cont += 1

print('-' * 50)
while True:
    escolha = int(input(' → Mostrar dados de qual jogador? '))
    print('-' * 50)
    if escolha == 999:
        print(f"{'<<< VOLTE SEMPRE >>>':^50}")
        break
    if 0 <= escolha < len(jogadores):
        print(f"         --- Levantamento jogador {jogadores[escolha]['nome']} ---")
        for indice, gol in enumerate(jogadores[escolha]['gols']):
            print(f"              No jogo {indice+1} fez {gol} gols.")
        print('-' * 50)
    else:
        print(' Código inválido! Tente novamente.')

print('=' * 50)
