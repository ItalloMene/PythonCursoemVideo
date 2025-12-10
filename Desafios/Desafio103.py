"""
Desafio 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome do jogador e quantos gols ele marcou.
O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""
def linha():
    print('=' * 55)
def ficha(jogador='<Desconhecido(a)>', gols=0):

    if jogador == '':
        jogador = '<Desconhecido(a)>'
    if gols == '':
        gols = '0'
    print(f' → Jogador(a) {jogador} fez {gols} gol(s) na partida.')
    linha()


# Programa principal
linha()
print(f'{"FICHA JOGADOR":^55}')
linha()
nome = str(input(' → Digite o nome do(a) jogador(a): ')).strip()
saldo = str(input(' → Digite o saldo de gols na partida: ')).strip()
linha()
ficha(jogador= nome,gols= saldo )

# Testes
ficha('Marta', 5)
ficha(gols=5)
ficha(jogador='João')
ficha()
