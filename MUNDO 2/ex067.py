while True:
    num = int(input('Quer ver a tabuada de qual valor? [DIGITE UM NÚMERO NEGATIVO PARA SAIR]: '))
    if num < 0:
        break
    print('-' * 20)
    for i in range(1, 11):
        print(f'{num} X {i:2} = {num * i}')
    print('-' * 20)

print('PROGRAMA ENCERRADO!')
