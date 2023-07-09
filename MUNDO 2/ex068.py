from random import randint
from time import sleep
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você \033[32mVENCEU\033[m!\n')
            v += 1
        else:
            print('Você \033[31mPERDEU\033[m!\n')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você \033[32mVENCEU\033[m!\n')
            v +=1
        else:
            print('Você \033[31mPERDEU\033[m!\n')
            break
    print('Vamos jogar novamente', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.\n')
    sleep(0.5)
print(f'GAME OVER! Você venceu \033[33m{v}\033[m vezes.')