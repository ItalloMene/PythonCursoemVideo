"""
Desafio 053: Crie um programa que leia uma frase qualquer e diga se ela é um PALINDROMO,
desconsiderando os espaços.
"""
"""
# Resposta 01: utilizando FOR
frase = str(input('Digite uma frase: ')).strip().upper()
#strip - tira os espaços no início e final da frase | upper - Deixa todas as letras da frase em Maiúsculo
palavras = frase.split()
# split - separa as palavras da frase num vetor(lista)
junto = ''.join(palavras)
# join - junta as palavras separadas numa 'string' só (nesse caso sem espaços)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    # Esse laço vai da última letra até a primeira voltando uma letra
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
# Verificador se a frase é ou não um palíndromo
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
"""
# Resposta 02: Utilizando o Fatiamento da linguagem Python
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')