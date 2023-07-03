p1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = p1 + (10 - 1) * razao

for i in range(p1, decimo + razao, razao):
    print('{} '.format(i), end='-> ')
print('ACABOU!')
