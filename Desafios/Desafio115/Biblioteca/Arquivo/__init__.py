from Biblioteca.Interface import *

def existeArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
        # rt = read text | Ler Texto
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        # wt+ = write text +| escrever texto +
        arquivo.close()
    except:
        linha()
        print('Houve um ERRO na criação do arquivo!')
    else:
        linha()
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        arquivo.close()


def cadastrar(arquivo, nome='Desconhecido', idade=0):
    try:
        arq = open(arquivo, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            arq.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            arq.close()
