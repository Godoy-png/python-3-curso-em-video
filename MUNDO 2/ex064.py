num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))

while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))

print('Você digitou \033[32m{}\033[m números e a soma entre eles foi \033[32m{}\033[m!'.format(cont, soma))
