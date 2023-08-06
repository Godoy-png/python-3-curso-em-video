listanum = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não será adicionado...')
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    if resposta in 'N':
        break

print('-=' * 30)
listanum.sort()
print(f'Você digitou os valores {listanum}')
