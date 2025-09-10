"""
Desafio 044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
- à vista dinheiro / cheque: 10% de desconto;
- à vista no cartão: 5% de desconto;
- em até 2x no cartão: preço normal;
- 3x ou mais no cartão: 20% de juros;
"""

texto = {
    'Negrito_S' : '\033[1;4m',
    'Azul' : '\033[94m',
    'Vermelho' : '\033[91m',
    'Verde' : '\033[92m',
    'Limpar' : '\033[m'
}

print('-' * 65)
print('                     {}PAGAMENTO DE PRODUTO{}'.format(texto['Azul'], texto['Limpar']))
print('-' * 65)
preco = float(input(' Digite o valor do produto: R$'))
print('-' * 65)
print('                     {}CONDIÇÕES DE PAGAMENTO{}'.format(texto['Azul'], texto['Limpar']))
print('-' * 65)
print(' {}1){} À vista dinheiro / cheque (Desconto de 10%); \n {}2){} À vista no cartão (5% de desconto);'
      .format(texto['Azul'], texto['Limpar'], texto['Azul'], texto['Limpar']))
print(' {}3){} Até 2x no cartão (preço normal) \n {}4){} 3x ou mais no cartão (20% de Juros)'
      .format(texto['Azul'], texto['Limpar'], texto['Azul'], texto['Limpar']))
print('-' * 65)
opcao = int(input(' Selecione uma das opções de pagamento a cima (1, 2, 3 ou 4): '))
print('-' * 65)

if opcao == 1:
    print(' {}Opção selecionada:{} à vista dinheiro / cheque. \n Com o desconto de 10%.'
          .format(texto['Negrito_S'], texto  ['Limpar']))
    desconto = preco - (preco * (10 / 100))
    print(' O cliente pagará {}R${:.2f}{} pelo produto que valia {}R${:.2f}{}.'
          .format(texto['Verde'],desconto, texto['Limpar'], texto['Verde'], preco, texto['Limpar']))
    print('-' * 65)

elif opcao == 2:
    print(' {}Opção selecionada:{} à vista no cartão. \n Com o desconto de 5% .'
          .format(texto['Negrito_S'], texto  ['Limpar']))
    desconto = preco - (preco * (5 / 100))
    print(' O cliente pagará {}R${:.2f}{} pelo produto que valia {}R${:.2f}{}.'
          .format(texto['Verde'],desconto, texto['Limpar'], texto['Verde'], preco, texto['Limpar']))
    print('-' * 65)

elif opcao == 3:
    print(' {}Opção selecionada:{} até 2x no cartão. \n Com o valor normal.'
          .format(texto['Negrito_S'], texto  ['Limpar']))
    parcela = preco / 2
    print(' O cliente pagará {}R${:.2f}{} por parcela sem descontos ou juros. \n Totalizando {}R${:.2f}{} do valor do produto.'
          .format(texto['Verde'], parcela, texto['Limpar'],texto['Verde'], preco, texto['Limpar']))
    print('-' * 65)

elif opcao == 4:
    print(' {}Opção selecionada:{} 3x ou mais no cartão. \n Com 20% de juros.'
          .format(texto['Negrito_S'], texto['Limpar']))
    quant_parcelas = int(input(' Digite a quantidade das parcelas: '))

    if quant_parcelas >= 3:
        val_juros = preco + preco * (20/100)
        val_parcelas = val_juros / quant_parcelas
        print(' O cliente pagará {}R${:.2f}{} por parcela. \n Totalizando {}R${:.2f}{} do valor do produto com o juros.'
              .format(texto['Verde'],val_parcelas,texto['Limpar'], texto['Verde'], val_juros, texto['Limpar'] ))

    else:
        print('{} [ERRO] Quantidade de parcelas não se adequa a opção selecionada.{} \n Por favor tente novamente!'
              .format(texto['Vermelho'], texto['Limpar']))
        print('-' * 65)

else:
    print('{} [ERRO] Opção selecionada não é valida.{} \n Por favor tente novamente!'
          .format(texto['Vermelho'], texto['Limpar']))
    print('-' * 65)