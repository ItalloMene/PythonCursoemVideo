"""
Desafio 090: Faça um programa que leia nome e média de um aluno, guardando também a situação num dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""
print('=' * 40)
aluno = str(input('→ Qual é o nome do(a) aluno(a): '))
media = float(input('→ Qual é a média do(a) aluno(a): '))
if media < 7:
    situacao = 'Reprovado'
else:
    situacao = 'Aprovado'
resultado = {'aluno': aluno, 'media':media, 'situacao':situacao}
print('=' * 40)
print(f'→ Nome salvo = {resultado['aluno']}')
print(f'→ Média de {resultado['aluno']} = {resultado['media']:.2f}')
print(f'→ Situação de {resultado['aluno']} = {resultado['situacao']}')
print(f'=' * 40)
#print(resultado)
