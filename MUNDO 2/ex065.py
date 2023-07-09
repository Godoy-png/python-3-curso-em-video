num = int(input('Digite um número: '))
resposta = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
soma = num
cont = 1
maior = menor = num

while resposta == 'S':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1

    if num > maior:
        maior = num
    if num < menor:
        menor = num
    resposta = str(input('Quer continuar [S/N]: ')).upper().strip()[0]

media = soma / cont

print('\nVocê digitou \033[32m{}\033[m números e a média foi \033[32m{:.2f}\033[m'.format(cont, media))
print('O maior valor foi \033[32m{}\033[m e o menor foi \033[32m{}'.format(maior, menor))

#27 de junho