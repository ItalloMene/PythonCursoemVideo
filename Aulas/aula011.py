"""
+ STYLE:
0 - None;
1 - Bold;
4 - Underline;
7 - Negative;

+ TEXT:
30 - Branco;
31 - Vermelho;
32 - Verde;
33 - Amarelo;
34 - Azul;
35 - Magenta(Roxo);
36 - Ciano;
37 - Cinza;

+ BACK:
40 - Branco;
41 - Vermelho;
42 - Verde;
43 - Amarelo;
44 - Azul;
45 - Magenta(Roxo);
46 - Ciano;
47 - Cinza;
"""

print('\033[1;31;43m Olá, Mundo! \033[m')
print('\033[4;30;45m Olá, Mundo! \033[m')
print('\033[0;33;44mOlá, Mundo! \033[m')
print('\033[7;33;44mOlá, Mundo! \033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Guanabara'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m',nome,'\033[m'))

nome = 'Guanabara'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'],nome, cores['limpa']))