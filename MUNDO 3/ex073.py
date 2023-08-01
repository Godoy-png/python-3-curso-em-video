times = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os últimos 4 colocados são: {times[-4:]}')
print(f'A lista em ordem alfabética é {sorted(times)}')
print(f'O time QUINZE está na {times.index("quinze")+1}ª posição')
