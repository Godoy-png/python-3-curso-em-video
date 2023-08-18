def area(a, b):
    r = a * b
    print(f'A área de um terreno {a}x{b} é de {r}m.')


print('Controle de Terrenos')
print('-' * 30)

area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))
