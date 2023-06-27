dist = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(dist))
passagem_curta = dist * 0.50
passagem_longa = dist * 0.45

if dist >200:
    print('Sua passagem irá custar R${:.2f}'.format(passagem_longa))
else:
    print('Sua passagem irá custar R${:.2f}'.format(passagem_curta))
