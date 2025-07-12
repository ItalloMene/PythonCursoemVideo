# DESAFIO 013 - Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário com 15% de aumento
salario = float(input('Por favor, digite o salário atual do funcionário: R$'))
aumento = salario * (15/100)
novosalario = salario + aumento
print('O novo salário com aumento de 15% é de R${:.2f}'.format(novosalario))