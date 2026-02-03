"""
Desafio 115: Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade num arquivo de
texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""

from Biblioteca.Interface import *
from Biblioteca.Arquivo import *
from time import sleep

arquivo = 'cadastros.txt'

if not existeArquivo(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = Menu(['Opção1', 'Opção2','Opção3'])
    if resposta == 1:
        # Listar pessoas Cadastradas
        lerArquivo(arquivo)
    elif resposta == 2:
        # Cadastro nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('→ Digite o Nome: '))
        idade = leiaInt('→ Digite a Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        # Sair do Sistema
        cabeçalho('Saindo do sistema... Até mais!')
        break
    else:
        # Digitou opção inválida
        print('ERRO! Digite uma opção válida!')
    sleep(1)

