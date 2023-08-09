temp = []
pricipal = []
mai = men = 0

while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso: ')))

    if len(pricipal) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    pricipal.append(temp[:])
    temp.clear()
    resposta = str(input('Quer continuar? [S/N]: ')).upper()
    if resposta in 'N':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pricipal)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for i in pricipal:
    if i[1] == mai:
        print(f'[{i[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for i in pricipal:
    if i[1] == men:
        print(f'[{i[0]}] ')
