from math import radians, sin, cos, tan

an = float(input('Digite o valor do ângulo: '))

seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))

print('O ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
print('O ãngulo de {} tem o COSSENO de {:.2f}'.format(an, cosseno))
print('O ângulo de {} tem a TANGENTE {:.2f}'.format(an, tangente))
