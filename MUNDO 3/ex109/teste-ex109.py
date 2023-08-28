from ex109 import moeda

p = float(input('Digite um preço: R$'))
print(f'\nA metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando em 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo em 5%, temos {moeda.diminuir(p, 5, True)}')
