from time import sleep

print('Iniciando a contagem regressiva...')
sleep(2)
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('BUUUM!')
