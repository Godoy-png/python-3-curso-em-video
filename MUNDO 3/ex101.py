def voto(nascimento):
    from datetime import datetime
    ano = datetime.now().year
    idade = ano - nascimento
    if idade < 16:
        print(f'Quem nasceu em {nascimento} tem {idade} anos e o voto NEGADO!')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Quem nasceu em {nascimento} tem {idade} anos e o voto OPCIONAL!')
    else:
        print(f'Quem nasceu em {nascimento} tem {idade} anos e o voto OBRIGATÓRIO!')


voto(int(input('Em que ano você nasceu? ')))
