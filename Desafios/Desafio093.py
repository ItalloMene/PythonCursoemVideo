"""
Desafio 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
quantidade de gols feitos em cada partida. No final, tudo isso será guardado num dicionário,
incluindo o total de gols feitos durante o campeonato.
"""
jogador = str(input('Digite o nome do jogador: '))
partidas = int(input(f'Digite quantas partidas {jogador} jogou: '))

gols = []
for cont in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols {jogador} fez na {cont}º partida? ')))

totgols = 0
for valor in gols:
    totgols += valor

dados = {'jogador':jogador, 'gols':gols[:], 'total':totgols}

print('-=' * 30)
print(dados)
print('-=' * 30)

for chave, valor in dados.items():
    print(f'O campo {chave} tem o valor {valor}')
print('-=' * 30)

print(f'O jogador {dados['jogador']} jogou {partidas}.')
for item, valor in enumerate(dados['gols']):
    print(f'  → Na partida {item + 1}, fez {valor} gols')
print(f'Foi um total de {dados['total']} gols')