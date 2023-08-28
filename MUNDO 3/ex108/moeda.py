def aumentar(preco=0, taxa=0):
    r = preco + (preco * taxa / 100)
    return r


def diminuir(preco=0, taxa=0):
    r = preco - (preco * taxa / 100)
    return r


def dobro(preco=0):
    r = preco * 2
    return r


def metade(preco=0):
    r = preco / 2
    return r


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')
