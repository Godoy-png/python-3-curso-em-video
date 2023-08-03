num = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),
       int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))

print(f'Você digitou os valores: {num}\n')
print(f'O número 9 apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'O número 3 foi digitado na {num.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado.')

print('Os valors pares digitados foram: ', end='')

cont = 0
for i in num:
    if i % 2 == 0:
        print(i, end=' ')
