"""
Desafio 059: Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair
O seu programa deverá realizar a operação solicitada em cada caso.
"""
escolha = 0
print('=' * 40)
print('\033[1;96m{:^40}\033[m'.format(' SOMAR, MULTIPLICAR, MAIOR'))
print('=' * 40)
n1 = float(input(' → Digite o primeiro valor: '))
n2 = float(input(' → Digite o segundo valor: '))
while escolha != 5:
    print('-' * 40)
    print(" [ 1 ] Somar \n [ 2 ] Multiplicar \n [ 3 ] Maior \n [ 4 ] Novos números \n [ 5 ] Sair")
    print('-' * 40)
    escolha = int(input(' → Digite o valor da sua escolha: '))
    print('-' * 40)
    if escolha == 1:
        soma = n1 + n2
        print('\033[1;93m A soma dos valores {:.1f} e {:.1f} é {:.1f}.\033[m'.format(n1, n2, soma))
        print('=' * 40)
    elif escolha == 2:
        multi = n1 * n2
        print('\033[1;93m A multiplicação de {:.1f} e {:.1f} é {:.1f}.\033[m'.format(n1, n2, multi))
        print('=' * 40)
    elif escolha == 3:
        if n1 > n2:
            print('\033[1;93m {:.1f} é o maior valor.\033[m'.format(n1))
            print('=' * 40)
        elif n2 > n1:
            print('\033[1;93m {:.1f} é o maior valor.\033[m'.format(n2))
            print('=' * 40)
        elif n1 == n2:
            print('\033[1;93m {:.1f} e {:.1f} são valores iguais.\033[m'.format(n1, n2))
            print('=' * 40)
    elif escolha == 4:
        n1 = float(input(' → Digite um novo primeiro valor: '))
        n2 = float(input(' → Digite um novo segundo valor: '))
        print('=' * 40)
    elif escolha == 5:
        print('\033[1;93m Você escolheu Sair. \n Fim da execução do programa!\033[m')
        print('=' * 40)
    else:
        print('\033[1;91m  Escolha inválida! Tente novamente!\033[m')
        print('=' * 40)
