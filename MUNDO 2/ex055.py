maior = 0
menor = 0
for i in range(1, 6):
    pesos = float(input('peso da {}ª pessoa: '.format(i)))
    if i == 1:
        maior = pesos
        menor = pesos
    else:
        if pesos > maior:
            maior = pesos
        if pesos < menor:
            menor = pesos
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
