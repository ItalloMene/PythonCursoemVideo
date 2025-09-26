"""
Desafio 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa mostre:
+ A média de idade do grupo;
+ Qual o nome do homem mais velho;
+ Quantas mulheres tem menos de 20 anos;
"""

soma_idades = 0
maior_idade = 0
mais_velho = '0'
feminino_menos20 = 0
print('=' * 45)
print('{:.45}'.format('ANALISADOR DE GRUPOS'))
print('=' * 45)
for cont in range(0,4):
    # Aquisição das Informações
    nome: str = str(input(' Digite seu nome: '))
    idade = int(input(' Digite sua idade: '))
    print(' [ 1 ] Masculino | [ 2 ] Feminino')
    sexo = int(input(' Selecione seu sexo: '))
    # Validação escolha do Sexo (Gênero)
    if (sexo < 1) or (sexo > 2):
        sexo = 0
        print(' [ERRO] ao registrar o sexo.')
    print('-' * 45)
    # Verificador "é o Homem mais velho?"
    if (sexo == 1) and (idade > maior_idade):
        mais_velho = nome
        maior_idade = idade
    # Verificador "Mulher abaixo dos 20 anos"
    if (sexo ==2) and (idade < 20):
        feminino_menos20 = feminino_menos20 + 1
    # Soma das idades + calculo da média
    soma_idades = soma_idades + idade
media_idades = soma_idades / 4
# Visualização dos Resultados
print('{:^45}'.format('RESULTADOS'))
print('-' * 45)
print(' A media de idades do grupo é: {:.0f} anos'.format(media_idades))
print(' {} é o homem mais velho go grupo.'.format(mais_velho))
print(' {} Mulher(es) do grupo tem menos de 20 anos'.format(feminino_menos20))
print('=' * 45)
