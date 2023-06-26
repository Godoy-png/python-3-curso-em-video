import math
oposto = float(input('Digite o comprimeito do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente'))
#hi = (oposto ** 2 + adjacente ** 2) ** (1/2)
hi = math.hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hi))
