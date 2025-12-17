import moedaD

val = float(input(" → Digite o valor do produto: R$"))
print(f" → Aumentando 20% de R${val} fica em {moedaD.aumentar(val, 20)}")
print(f" → Diminuindo 20% de R${val} fica em {moedaD.diminuir(val,20)}")
print(f" → O dobro de R${val} fica em {moedaD.dobrar(val)}")
print(f" → A metade de R${val} fica em {moedaD.metade(val)}")
