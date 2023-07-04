sexo = ''
while sexo != 'M' and sexo != 'F' and sexo != 'OUTRO':
    sexo = input('Informe o seu sexo\n[M / F / Outro]: ').upper().strip()
    if sexo != 'M' and sexo != 'F' and sexo != 'OUTRO':
        print('Dados inválidos, tente novamente!')
print('Dados cadastrados com sucesso!')
