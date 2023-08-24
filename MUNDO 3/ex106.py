from time import sleep

c = ('\033[m',  # 0 - SEM COR
     '\033[0;30;45m',  # 1 - ROXO
     '\033[7;40m')  # 2 - BRANCO


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 1)
    print(c[2], end='')
    help(com)
    print(c[0], end='')
    sleep(1.5)


def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('-' * (tam+4))
    print(f'  {msg}')
    print('-' * (tam+4))
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('AJUDA PYTHON', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)


titulo('FIM DO PROGRAMA!', 1)
