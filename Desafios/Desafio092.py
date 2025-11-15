"""
Desafio 092: Crie um programa que leia nome, ano de nascimento, e carteira de trabalho
e cadastre-os (com idade) num dicionário se por acaso o CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date

print('=' * 40)
nome = str(input('→ Digite seu nome: '))
nascimento = int(input('→ Digite seu ano de nascimento: '))
idade = date.today().year - nascimento
ctps = int(input('→ Carteira de trabalho (0 não tem): '))

dados = {'nome':nome, 'idade':idade, 'ctps':ctps}

if ctps > 0:
    contratacao = int(input('→ Digite seu ano de contratação: '))
    dados['contratação'] = contratacao
    salario = float(input('→ Digite seu salário: R$'))
    dados['salário'] = salario
    aposentadoria = (contratacao + 35) - nascimento
    dados['aposentadoria'] = aposentadoria

print('=' * 40)
for chave, valor in dados.items():
    print(f'+ {chave} tem o valor {valor}')
print('=' * 40)
#print(dados)

