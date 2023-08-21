from time import sleep


def maior(* num):
    cont = maior = 0
    print('-' * 30)
    print('Analisando os valores passados... ')
    for i in num:
        print(f'{i} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 1)
maior(4, 7, 0)
maior()
