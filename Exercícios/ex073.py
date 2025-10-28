"""
Desafio 073: Crie uma Tupla preenchida com os 20 primeiros colocados da tabela do campeonato
Brasileiro de futebol (2017), na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados;
B) Os últimos 4 colocados da tabela;
C) Uma lista com os times em ordem alfabética;
D) Em que posição na tabela está o time da Chapecoense.;
"""

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense',
         'Atlético Mineiro', 'Botafogo', 'Atlético Paranaense', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport',
         'Vitória', 'Coritiba', 'Avai', 'Ponte Preta',
         'Atlético Goianiense')
# Por extenso
print('-=' * 15)
print(f' Lista de times: {times}.')
print('-=' * 15)
print(f' Os 5 primeiros times são {times[0:5]}')
print('-=' * 15)
print(f' Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f' Times em ordem alfabética {sorted(times)}')
print('-=' * 15)
print(f' O Chapecoense está na {times.index('Chapecoense') + 1} posição.')
print('-=' * 15)
'''
# Mostrar um time abaixo do outro
print('-=' * 15) 
for t in times: 
    print(t)
print('-=' * 15)
'''

