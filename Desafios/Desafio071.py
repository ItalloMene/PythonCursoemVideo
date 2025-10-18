"""
Desafio 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início pergunta ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa tem cédulas de R$50, R$20, R$10, R$1.
"""
print("=" * 50)
print(f'\033[1;92m{'CAIXA ELETRÔNICO':^50}\033[m')
print('=' * 50)

valor = int(input(' → Qual é o valor a ser sacado? R$'))
print('=' * 50)
saquetotal = valor
cinquenta = vinte = dez = um = 0
while True:
    if valor >= 50:
        valor -= 50
        cinquenta += 1
    elif valor >= 20:
        valor -= 20
        vinte += 1
    elif valor >= 10:
        valor -= 10
        dez += 1
    elif valor >= 1:
        valor -= 1
        um += 1
    if valor == 0:
        break

print(f' → Serão entregues \033[92m{cinquenta}\033[m cédulas de \033[92mR$50,00\033[m')
print(f' → Serão entregues \033[92m{vinte}\033[m cédulas de \033[92mR$20,00\033[m')
print(f' → Serão entregues \033[92m{dez}\033[m cédulas de \033[92mR$10,00\033[m')
print(f' → Serão entregues \033[92m{um}\033[m cédulas de \033[92mR$1,00\033[m')
print('=' * 50)
print(f' → Totalizando o saque de \033[92mR${saquetotal:.2f}\033[m')
print('=' * 50)

