cont = soma = 0

while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'Você digitou \033[32m{cont}\033[m números e a soma deles foi \033[32m{soma}\033[m.')
