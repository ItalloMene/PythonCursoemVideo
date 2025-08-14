"""
DESAFIO 034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00 calcule um aumento de 10%.
Para inferiores ou iguais o aumento é de 15%.
"""

salario = float(input('Digite o salário atual do funcionário: '))
print('Com o salário de R${:.2f}'.format(salario))
if salario > 1250:
    ajuste = salario + (salario * (10/100))
    print('O novo valor do salário será R${:.2f}'.format(ajuste))
else:
    ajuste = salario + (salario * (15/100))
    print('O novo valor do salário será R${:.2f}'.format(ajuste))