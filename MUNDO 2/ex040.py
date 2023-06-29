n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f} sua média será de {:.1f}'.format(n1, n2, media))

if media < 5:
    print('Você está REPROVADO!')
elif media >= 7:
    print('Você está APROVADO!')
else:
    print('Você está de RECUPERAÇÃO!')
