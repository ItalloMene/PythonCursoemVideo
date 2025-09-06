"""
Desafio 039: Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade:
- Se ele ainda vai se alistar no serviço militar;
- Se é a hora de se alistar;
- Se já passou do tempo do alistamento
O seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import datetime
print('+' * 25)
print(' \033[93mCHECAGEM DE ALISTAMENTO\033[m ')
print('+' * 25)

nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - nascimento

print(' ')
print('        \033[4;93mRESPOSTA\033[m')
if idade < 18:
    print('Você ainda irá se alistar.')
    print('Tendo \033[4;93m{}\033[m anos de idade ainda faltam \033[4;92m{}\033[m anos até você precisar se alistar.'.format(idade, 18 - idade))
elif idade > 18:
    print('Você já passou do tempo do alistamento.')
    print('Tendo \033[4;93m{}\033[m anos de idade você já passou \033[91;4m{}\033[m anos do alistamento.'.format(idade, idade - 18))
else:
    print('Você já está no tempo do alistamento.')
    print('Tendo \033[4;93m{}\033[m anos você está na idade de se alistar.'.format(idade))
