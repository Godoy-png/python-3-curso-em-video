def aumentar(preco=0, taxa=0, formato=False):
    r = preco + (preco * taxa / 100)
    return r if formato is False else moeda(r)


def diminuir(preco=0, taxa=0, formato=False):
    r = preco - (preco * taxa / 100)
    return r if formato is False else moeda(r)


def dobro(preco=0, formato=False):
    r = preco * 2
    return r if formato is False else moeda(r)


def metade(preco=0, formato=False):
    r = preco / 2
    return r if formato is False else moeda(r)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, aume=10, dimi=5):
    print('-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aume}% de aumento: \t{aumentar(preco, aume, True)}')
    print(f'{dimi}% de desconto: \t{diminuir(preco, dimi, True)}')
