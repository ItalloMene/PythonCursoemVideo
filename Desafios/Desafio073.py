"""
Desafio 073: Crie uma Tupla preenchida com os 20 primeiros colocados da tabela do campeonato
Brasileiro de futebol (2017), na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados;
B) Os últimos 4 colocados da tabela;
C) Uma lista com os times em ordem alfabética;
D) Em que posição na tabela está o time da Chapecoense.;
"""

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama',
         'Chapecoense', 'Atlético Mineiro', 'Botafogo', 'Atlético Paranaense', 'Bahia', 'São Paulo',
         'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avai', 'Ponte Preta', 'Atlético Goianiense')
print('=' * 75)
print(f' Os 5 primeiros colocados são:\n 1º {times[0]} | 2º {times[1]} | 3º {times[2]} | 4º {times[3]} | 5º {times[4]}')
print('-' * 75)
print(f' Os 4 últimos colocados são:\n 17ª {times[16]} | 18º {times[17]} | 19º {times[18]} | 20º {times[19]}')
print('-' * 75)
print(' Lista dos times em ordem alfabética: ')
alfabetico = sorted(times)
for c in range(0, 20):
    print(f' > {alfabetico[c]}')
print('-' * 85)
print(f' O time da Chapecoense estava em 8º lugar na tabela do campeonato brasileiro de 2017')
print('=' * 85)