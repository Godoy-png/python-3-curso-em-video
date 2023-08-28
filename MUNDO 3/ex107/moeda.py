def aumentar(preco, taxa):
    r = preco + (preco * taxa / 100)
    return r


def diminuir(preco, taxa):
    r = preco - (preco * taxa / 100)
    return r


def dobro(preco):
    r = preco * 2
    return r


def metade(preco):
    r = preco / 2
    return r
