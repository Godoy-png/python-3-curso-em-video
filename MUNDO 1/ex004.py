algo = input('Digite algo: ')

print('O tipo primitivo desse valor é', type(algo))
print('Só tem espaços?', algo.isspace())
print('É um número?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Está somente em maiúsculas?', algo.isupper())
print('Está somente em minúsculas?', algo.islower())
print('Está capitalizada?', algo.istitle())

