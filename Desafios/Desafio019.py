# DESAFIO 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
aluno1 = input('Digite o nome do(a) primeiro aluno(a): ')
aluno2 = input('Digite o nome do(a) segundo aluno(a): ')
aluno3 = input('Digite o nome do(a) terceiro aluno(a): ')
aluno4 = input('Digite o nome do(a) quarto aluno(a): ')
alunos = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.shuffle(alunos)
#print('{}, {}, {}, {}.'.format(aluno1, aluno2, aluno3, aluno4))
print('Ordem sorteada é: 1º{}, 2º{}, 3º{}, 4º{}'.format(alunos[0], alunos[1], alunos[2], alunos[3]))
