from datetime import datetime
dados = dict()

dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de Trabalho [0 não tem]: '))
if dados['ctps'] == 0:
    print('-=' * 30)
    for k, v in dados.items():
        print(f'- {k} tem o valor {v}')
else:
    dados['contrato'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + (dados['contrato'] + 35) - datetime.now().year

    print('-=' * 30)
    for k, v in dados.items():
        print(f'- {k} tem o valor {v}')
