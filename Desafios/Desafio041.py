"""
Desafio 041: A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre a sua categoria, de acordo com a idade:
- Até 9 anos - Mirim;
- Até 14 anos - Infantil;
- Até 19 anos - Junior;
- Até 20 anos - Sênior;
- Acima - Master
"""
from datetime import datetime
print('=' * 22)
print(' \033[93mCATEGORIA DO ATLETA\033[m')
print('=' * 22)
nascimento = int(input('Por favor, digite o ano de nascimento do atleta: '))
ano_atual = datetime.now().year
idade = ano_atual - nascimento
print('Idade do Atleta: \033[1;4m{} anos\033[m.'.format(idade))

if (idade > 0) and (idade <= 9):
    print('Pela idade o atleta está na categoria \033[1;4mMirim\033[m.')
elif (idade > 9) and (idade <= 14):
    print('Pela idade o atleta está na categoria \033[1;4mInfantil\033[m.')
elif (idade > 14) and(idade <= 19):
    print('Pela idade o atleta está na categoria \033[1;4mJunior\033[m.')
elif (idade > 19) and (idade <= 20):
    print('Pela idade o atleta está na categoria \033[1;4mSênior\033[m.')
elif idade > 20:
    print('Pela idade o atleta está na categoria \033[1;4mMaster\033[m.')
else:
    print('\033[31m[ERRO] Não foi possível verificar a categoria do atleta!\033[m')

