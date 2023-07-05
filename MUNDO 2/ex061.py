print('GERADOR DE PA DE \033[32m10 TERMOS\033[m\n')

p1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = p1
cont = 1

while cont <= 10:
    print('\033[32m{}\033[m -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM!')