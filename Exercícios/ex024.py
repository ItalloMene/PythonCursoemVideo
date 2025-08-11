"""
DESAFIO 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "SANTO"
"""

# RESPOSTA 01:
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')