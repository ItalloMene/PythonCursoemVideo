"""
Desafio 114: Crie um código em Python que teste se o site Pudim está acessível pelo computador utilizado
"""
import urllib, urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
   #print(site.read()) - mostra o conteúdo HTML do site
