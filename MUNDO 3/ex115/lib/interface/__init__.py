def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! DIGITE UM NÚMERO INTEIRO.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mAÇÃO INTERROMPIDA PELO USUÁRIO.\033[m')
            return 0
        else:
            return n


def linha(tamanho=42):
    return '-' * tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[35m{c}\033[m - {i}')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
