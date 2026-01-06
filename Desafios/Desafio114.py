"""
Desafio 114: Crie um código em Python que teste se o site Pudim está acessível pelo computador utilizado
"""
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[1;91m→ Não foi possível acessar o site Pudim.\033[m')
else:
    print('\033[1;92m→ Site Pudim acessado com sucesso!\033[m')
