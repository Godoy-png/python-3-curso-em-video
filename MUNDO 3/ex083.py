expressao = str(input('Digite a expressão: '))
contador = []

for i in expressao:
    if i == '(':
        contador.append('(')
    elif i == ')':
        if len(contador) > 0:
            contador.pop()
        else:
            contador.append(')')
            break

if len(contador) == 0:
    print('Expressão válida!')
else:
    print('Expressão errada!')
