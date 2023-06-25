altura = float(input('Qual altura da parede?: '))
largura = float(input('Qual a largura da parede?: '))
area = largura * altura

print('Sua parede tem a área de {}m².'
      '\nPara pintar essa parede serão necessários {} litros de tinta'.format(area, area/2))
