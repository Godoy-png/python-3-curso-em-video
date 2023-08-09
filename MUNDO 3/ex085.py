num = [[], []]
valor = 0

for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')

'''
princ = []
par = []
impar = []

for i in range(0, 7):
    princ.append(int(input(f'Digite o {i+1}º valor: ')))

for i in princ:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

princ.clear()
par.sort()
impar.sort()
princ.append(par[:])
princ.append(impar[:])

print('-=' * 30)
print(f'Os valores pares são: {princ[0]}')
print(f'Os valors ímpares são: {princ[1]}')
'''
