"""
Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
- Média abaixo de 5,0: reprovado;
- Média entre 5,0 e 6,9: recuperação;
- Média 7,0 ou superior: aprovado;
"""
print('=' * 35)
print('\033[96m{:^35}\033[m'.format('AVALIADOR DE MÉDIA'))
print('=' * 35)
aluno = str(input('Digite o nome do(a) aluno(a): '))
nota1 = float(input('Digite a primeira nota de {}:'.format(aluno)))
nota2 = float(input('Digite a segunda nota de {}: '.format(aluno)))
media = (nota1 + nota2) / 2
print('=' * 35)
print(' \033[96m{:^35}\033[m'.format('RESULTADO'))
print('=' * 35)
if (media >= 0) and (media < 5.0):
    print('{} está \033[4;91mREPROVADO\033[m! \nSua média foi de \033[4;91m{:.1f}\033[m.'.format(aluno, media))
elif (media >= 5.0) and (media < 6.9):
    print('{} está de \033[4;93mRECUPERAÇÃO\033[m! \nSua média foi de \033[4;93m{:.1f}\033[m.'.format(aluno, media))
elif (media >= 7.0) and (media <= 10):
    print('{} está \033[4;92mAPROVADO\033[m! \nSua média foi de \033[4;92m{:.1f}\033[m.'.format(aluno, media))
else:
    print('\033[1;97;41m[ERRO] Média não pode ser calculada!\033[m \n\033[1;97;42mPor favor tente novamente!\033[m')
