"""
Desafio 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Obs: Adicione também as docstring da função.
"""

def linha():
    print('=' * 100)

def notas(*nota, sit=False):
    """
    → Função para analisar notas para mostrar a maior e a menor e a média da turma num dicionário
    com situação geral de forma opcional.
    :param nota: Recebe uma ou mais notas
    :param sit: Opcional que recebe a escolha de mostrar ou não a situação da turma
    :return: Dicionário com as informações da turma que a função analisou.
    """
    info = {}

    total = len(nota)
    info['Total'] = total

    somaNota = 0
    for chave, valor in enumerate(nota):
        if chave == 0:
            maior = menor = valor
        else:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
        somaNota += valor

    media = somaNota / total

    info['Maior'] = maior
    info['Menor'] = menor
    info['Média'] = f'{media:.2f}'

    if sit:
        if media < 5:
            info['Situação'] = 'RUIM!'
        elif media >= 7:
            info['Situação'] = 'BOA!'
        else:
            info['Situação'] = 'RAZOÁVEL!'

    return info


# Programa principal
linha()
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
linha()
resp = notas(3.5, 10, 6.5, sit=True)
print(resp)
linha()
resp = notas(3.5, 2, 6.5, sit=True)
print(resp)
linha()
resp = notas(4.5, 7, 10, 8, 3, 2)
print(resp)
linha()
help(notas)
linha()
