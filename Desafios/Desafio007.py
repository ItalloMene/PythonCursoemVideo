# DESAFIO 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media

aluno = input('Por favor digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota de {}: '.format(aluno)))
nota2 = float(input('Digite a segunda nota de {}: '.format(aluno)))
media = (nota1 + nota2) / 2
print('A \033[1;4;33m Média \033[m das notas de \033[1;4;36m {} \033[m é \033[1;4;33m {:.2f} '.format(aluno, media))
