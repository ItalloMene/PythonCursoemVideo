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


def resumo(preço, aum, dim):
    print('=' * 30)
    print(f"{'RESUMO DO VALOR':^30}")
    print('=' * 30)
    print(f'{"Preço analisado:":<20} {moeda(preço)}')
    print(f'{"Dobro do preço:":<20} {dobrar(preço, True)}')
    print(f'{"Metade do preço:":<20} {metade(preço, True)}')
    print(f'{aum}{"% de aumento:":<18} {aumentar(preço, aum, True)}')
    print(f'{dim}{"% de redução:":<18} {diminuir(preço, dim, True)}')
    print('=' * 30)
