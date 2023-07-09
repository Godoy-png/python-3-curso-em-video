tot18 = 0
totmasc = 0
totmu20 = 0
cont = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    cont += 1

    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totmasc += 1
    if sexo == 'F' and idade < 20:
        totmu20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        print('-' * 20)
    if resp == 'N':
        break

print(f'\nVocê cadastrou \033[32m{cont}\033[m PESSOAS, das quais:\n')
print(f'\033[32m{tot18}\033[m pessoas tem MAIS de 18 anos.')
print(f'\033[32m{totmasc}\033[m HOMENS foram cadastrados.')
print(f'\033[32m{totmu20}\033[m MULHERES tem MENOS de 20 anos.')
