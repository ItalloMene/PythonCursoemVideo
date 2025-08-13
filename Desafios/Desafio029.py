"""
DESAFIO 029 - Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""
velocidade = int(input('Digite a Velocidade do carro (Km/h): '))
print('Analisando...\n {}Km/h'.format(velocidade))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Voê foi Multado!')
    print('Valor da Multa R${:.2f}'.format(multa))
else:
    print('Velocidade dentro do limite de velocidade permitido!')
