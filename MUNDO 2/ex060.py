# from math import factorial
#n = int(input('Digite um número para calcular seu FATORIAL: '))
#f = factorial(n)
#print('O factorial de {} é {}'.format(n, f))

from time import sleep
n = int(input('Digite um número para calcular seu FATORIAL: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    sleep(0.5)
    f *= c
    c -= 1
print(f)
