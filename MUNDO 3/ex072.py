numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

escolha = int(input('Digite um número entre 0 e 20: '))
while escolha < 0 or escolha > 20:
    escolha = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Você digitou o número \033[32m{numeros[escolha]}\033[m!')
