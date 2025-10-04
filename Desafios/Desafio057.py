"""
Desafio057: faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
print('=' * 50)
print('\033[93m{:^50}\033[m'.format('REGISTRO DE SEXO'))
print('=' * 50)
sexo = ' '
while (sexo != 'M') and (sexo !='F'):
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    print('-' * 50)
    if sexo == 'M':
        print('\033[92mSexo registrado com sucesso como Masculino!\033[m')
        print('=' * 50)
    elif sexo == 'F':
        print('\033[92mSexo registrado com sucesso como Feminino!\033[m')
        print('=' * 50)
    else:
        print('\033[91m[ERRO] Sexo não pode ser registrado dessa forma!\033[m '
              '\nPor favor tente novamente entre [M/F]')
        print('-' * 50)