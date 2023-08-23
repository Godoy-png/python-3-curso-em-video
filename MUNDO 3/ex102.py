def fatorial(n, show=False):
    """
    -> CALCULA O FATORIAL DE UM NÚMERO.
    :param n: O número a ser calculado.
    :param show: Mostrar ou não a conta (OPCIONAL).
    :return: O valor do FATORIAL de um número n.
    """
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f


print(fatorial(5, show=True))
print(fatorial(5))
