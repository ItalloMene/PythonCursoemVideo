"""
Desafio 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo numa lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada
aluno individualmente.
"""
texto = {
    'titulo' : '\033[1;96m',
    'bolder' : '\033[1m',
    'limpar' : '\033[m'
}

boletim = []
alunos = []

print(f'{texto['titulo']}=' * 60)
print(f'{"BOLETIM ESCOLAR":^60}')
print('=' * 60, texto['limpar'])

# Adição do nome, notas e medias dos alunos a lista composta boletim
while True:
    aluno = str(input(f'{texto['bolder']} → Digite o nome do(a) aluno(a): '))
    alunos.append(aluno)
    nota1 = float(input(' → Digite a primeira nota: '))
    alunos.append(nota1)
    nota2 = float(input(' → Digite a segunda nota: '))
    alunos.append(nota2)
    media = (nota1 + nota2) / 2
    alunos.append(media)

    while True:
        resposta = str(input(f' → Deseja continuar (Sim/Não)? {texto['limpar']}')).strip().upper()[0]
        if resposta in 'SN':
            break

    boletim.append(alunos[:])
    alunos.clear()

    if resposta in 'N':
        break

# Mostrar alunos e sua respectiva média
print(f'{texto['titulo']}=' * 60)
print(f' {"Nº":<17} {"Aluno":^17} {"Médias":>17}')
print('=' * 60, texto['limpar'])

for item in range(0, len(boletim)):
    print(f'{texto['bolder']} {item:<17} {boletim[item][0]:^17} {boletim[item][3]:>17.1f} {texto['limpar']}')

# Mostrar notas do aluno escolhido
print(f'{texto['titulo']}=' * 60)
print(f' {"Digite 999 para finalizar o programa":^60} ')
print('=' * 60, texto['limpar'])

while True:
    escolha = int(input(f'{texto['bolder']} → Digite o número do aluno para ver suas notas: '))
    if escolha == 999:
        print(f'{texto['titulo']}=' * 60)
        print(f' {"OBRIGADO VOLTE SEMPRE!":^60}')
        break
    else:
        print(f' + As notas de {boletim[escolha][0].upper()} são: {boletim[escolha][1]} e {boletim[escolha][2]} {texto['limpar']}')
print('=' * 60, texto['limpar'])