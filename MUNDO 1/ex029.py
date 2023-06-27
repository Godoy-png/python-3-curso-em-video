velocidade = float(input('Qual a velocidade atual do carro? '))
multa = (velocidade - 80) * 7

if velocidade <= 80:
    print('Tenha um bom dia!')
else:
    print('Você passou do limite de 80Km/h.')
    print('Você recebeu uma MULTA de R${:.2f}!'.format(multa))
    print('Dirija com segurança.')
