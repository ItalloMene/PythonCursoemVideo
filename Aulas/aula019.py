"""
pessoas = {'nome':'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print('-' * 20)
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-' * 20)
"""
"""
for k in pessoas.keys():
    print(k)
print('-' * 20)
for k in pessoas.values():
    print(k)
print('-' * 20)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-' * 20)
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-' * 20)
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-' * 20)
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-' * 20)
"""
"""
brasil = [] # Ou brasil = list()
estado1 = {'uf':'Rio de janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
print('-' * 20)
"""

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # cópia para o dicionário
print(brasil)
print('-' * 20)
for e in brasil:
    print(e)
print('-' * 20)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
print('-' * 20)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
