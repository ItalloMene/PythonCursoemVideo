import moedaE

p = float(input("Digite o preço: R$"))
print(f'A metade de R${p} é {moedaE.metade(p)}')
print(f'O dobro de R${p} é {moedaE.dobro(p)}')
print(f'Aumentando 10%, temos {moedaE.aumentar(p, 10)}')
print(f'Diminuindo 10%, temos {moedaE.diminuir(p, 10)}')
