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


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! DIGITE UM NÚMERO REAL.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mAÇÃO INTERROMPIDA PELO USUÁRIO.\033[m')
            return 0
        else:
            return n


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'\nO valor inteiro digitado foi: {inteiro}')
print(f'O valor real digitado foi: {real}')
