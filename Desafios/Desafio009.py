# DESAFIO 009 - Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.
cores = {
    'limpar' : '\033[m',
    'tciano' : '\033[1;36;40m',
    'tverde' : '\033[1;32;40m',
    'tazul' : '\033[1;34;40m',
    'troxo' : '\033[1;35;40m'
}
num = int(input('Por favor, digite um número: '))
print('{}{}{} x 1 = {}{}'.format(cores['tverde'],num, cores['tciano'], cores['tazul'], num * 1))
print('{}{}{} x 2 = {}{}'.format(cores['tverde'],num, cores['tciano'], cores['tazul'], num * 2))
print('{}{}{} x 3 = {}{}'.format(cores['tverde'],num, cores['tciano'], cores['tazul'], num * 3))
print('{}{}{} x 4 = {}{}'.format(cores['tverde'],num, cores['tciano'], cores['tazul'], num * 4))
print('{}{}{} x 5 = {}{}'.format(cores['tverde'],num, cores['tciano'], cores['tazul'], num * 5))
print('{}{}{} x 6 = {}{}'.format(cores['tverde'],num, cores['tciano'], cores['tazul'], num * 6))
print('{}{}{} x 7 = {}{}'.format(cores['tverde'],num, cores['tciano'], cores['tazul'], num * 7))
print('{}{}{} x 8 = {}{}'.format(cores['tverde'],num, cores['tciano'], cores['tazul'], num * 8))
print('{}{}{} x 9 = {}{}'.format(cores['tverde'],num, cores['tciano'], cores['tazul'], num * 9))
print('{}{}{} x 10 = {}{}'.format(cores['tverde'],num, cores['tciano'], cores['tazul'], num * 10))