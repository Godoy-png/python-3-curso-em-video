dias = int(input('Por quantos dias o carro foi alugado?: '))
km = float(input('Quantos KM o carro percorreu?: '))
pre_dia = dias * 60
pre_km = km * 0.15

print('Você deve pagar o valor de R${:.2f}.'.format(pre_dia + pre_km))
# 16 DE MAIO DE 2023
