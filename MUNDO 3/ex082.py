listaTodos = []
listaImpar = []
listaPar = []

while True:
    listaTodos.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    if resposta in 'N':
        break

for i in listaTodos:
    if i % 2 == 0:
        listaPar.append(i)
#   else:
#       listaImpar.append(i)

for p in listaTodos:
    if not p % 2 == 0:
        listaImpar.append(p)

print('-=' * 30)
print(f'Lista completa: {listaTodos}')
print(f'Lista Ímpar: {listaImpar}')
print(f'Lista Par: {listaPar}')
