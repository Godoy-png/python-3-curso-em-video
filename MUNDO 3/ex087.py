matr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0

for i in range(0, 3):
    for c in range(0, 3):
        matr[i][c] = int(input(f'Digite um valor para [{i}, {c}]: '))

print('-=' * 30)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matr[i][c]:^8}]', end='')

        if matr[i][c] % 2 == 0:
            spar += matr[i][c]
    print()

print('-=' * 30)
print(f'A soma dos valores pares é: {spar}')

for i in range(0, 3):
    scol += matr[i][2]
print(f'A soma dos valores da terceira coluna é: {scol}')

for c in range(0, 3):
    if c == 0:
        mai = matr[1][c]
    elif matr[1][c] > mai:
        mai = matr[1][c]
print(f'O maio valor da segunda linha é: {mai}')
