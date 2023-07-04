from random import randint

computador = randint(0, 10)
tentativas = 1

print('Tente adivinhar o número que estou pensando. Entre 0 e 10!')
palpite = int(input('Palpite: '))

while palpite != computador:
    if palpite > computador:
        print('\nO número que estou pensando é menor que {}!'.format(palpite))
    else:
        print('\nO número que estou pensando é maior que {}!'.format(palpite))
    palpite = int(input('Tente novamente: '))
    tentativas += 1

print('\nParabéns você acertou em {} tentativas.'.format(tentativas))
print('Eu estava pensando no número {}!!'.format(palpite))
