def moeda(preço):
    val =  f"R${preço:.2f}"
    return val


def aumentar(preço, taxa):
    res = preço + (preço * taxa/100)
    val = moeda(res)
    return val


def diminuir(preço,taxa):
    res = preço - (preço * taxa/100)
    val = moeda(res)
    return val


def dobrar(preço):
    res = preço * 2
    val = moeda(res)
    return val


def metade(preço):
    res = preço / 2
    val = moeda(res)
    return val

