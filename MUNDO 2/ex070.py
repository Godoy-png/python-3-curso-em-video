total = caro = valorbarato = cont = 0
nomebarato = ''

while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço R$: '))
    total += preco
    cont += 1

    if preco > 1000:
        caro += 1

    if cont == 1 or preco < valorbarato:
        valorbarato = preco
        nomebarato = nome

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        print('-' * 20)
    if resp == 'N':
        break

print(f'\nO TOTAL da compra foi \033[32mR${total:.2f}\033[m')
print(f'\033[32m{caro:.2f}\033[m produtos custam MAIS de R$1000.00')
print(f'O produto mais BARATO foi \033[32m{nomebarato}\033[m que custa \033[32mR${valorbarato:.2f}\033[m')
