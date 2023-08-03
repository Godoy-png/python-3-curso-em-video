itens = ('Lápis', 1.50, 'Mochila', 112.50, 'Livro', 35.00,
         'Caneta', 1.00, 'Borracha', 0.50)

print('-' * 40)
print(f'{"LISTAGEM DE PRERÇOS":^40}')
print('-' * 40)

for i in range(0, len(itens)):
    if i % 2 == 0:
        print(f'{itens[i]:.<30}', end='')
    else:
        print(f'R${itens[i]:>7.2f}')

print('-' * 40)
