# DESAFIO 020 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
aluno1 = input('Digite o nome do(a) primeiro aluno(a): ')
aluno2 = input('Digite o nome do(a) segundo aluno(a): ')
aluno3 = input('Digite o nome do(a) terceiro aluno(a): ')
aluno4 = input('Digite o nome do(a) quarto aluno(a): ')
alunos = [aluno1, aluno2, aluno3, aluno4]
print('Os alunos que irão apresentar são: {}, {}, {} e {}.'.format(alunos[0], alunos[1], alunos[2], alunos[3]))
sorteio = random.shuffle(alunos)
print('A ordem das apresentações será 1º{}, 2º{}, 3º{} e 4º{}'.format(alunos[0], alunos[1], alunos[2], alunos[3]))