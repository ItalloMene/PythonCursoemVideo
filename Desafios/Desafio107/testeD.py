import moedaD

val = float(input(" → Digite o valor do produto: R$"))
print(f" → Aumentando 20% de {val} fica em R${moedaD.aumentar(val, 20)}")
print(f" → Diminuindo 20% de {val} fica em R${moedaD.diminuir(val,20)}")
print(f" → O dobro de {val} fica em R${moedaD.dobrar(val)}")
print(f" → A metade de {val} fica em R${moedaD.metade(val)}")
