print('GERADOR DE PA DE \033[32m10 TERMOS\033[m\n')

p1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = p1
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('\033[32m{}\033[m -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('\nProgressão finalizada com \033[32m{}\033[m termos mostrados!'.format(total))
print('FIM!')
