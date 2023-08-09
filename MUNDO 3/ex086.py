matr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for c in range(0, 3):
        matr[i][c] = int(input(f'Digite um valor para [{i}, {c}]: '))

print('-=' * 30)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matr[i][c]:^8}]', end='')
    print()
