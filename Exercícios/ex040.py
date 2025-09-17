"""
Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
- Média abaixo de 5,0: reprovado;
- Média entre 5,0 e 6,9: recuperação;
- Média 7,0 ou superior: aprovado;
"""
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média: float = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 5: # | if 5 <= média < 7: | if média >= 5 and média < 7:
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno está REPROVADO.')
elif média >= 7:
    print('O aluno está APROVADO.')