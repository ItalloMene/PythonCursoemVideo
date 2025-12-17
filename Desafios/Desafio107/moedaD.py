def moeda(preço):
    val =  f"R${preço:.2f}"
    return val


def aumentar(preço, taxa, form=False):
    res = preço + (preço * taxa/100)
    if form:
        val = moeda(res)
        return val
    else:
        return res


def diminuir(preço,taxa, form=False):
    res = preço - (preço * taxa/100)
    if form:
        val = moeda(res)
        return val
    else:
        return res


def dobrar(preço, form=False):
    res = preço * 2
    if form:
        val = moeda(res)
        return val
    else:
        return res


def metade(preço, form=False):
    res = preço / 2
    if form:
        val = moeda(res)
        return val
    else:
        return res

