listanum = list()

while True:
    listanum.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    if resposta in 'N':
        break

print('-=' * 30)
print(f'Você digitou {len(listanum)} números.')

listanum.sort(reverse=True)
print(f'A lista em ordem decrescente é {listanum}')

if 5 in listanum:
    print(f'O valor 5 foi digitado e está na lista!')
else:
    print('O valor 5 não faz parte da lista!')
