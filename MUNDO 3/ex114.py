import urllib.request

try:
    sire = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site não está acessível no momento.')
else:
    print('O site foi acessado com sucesso.')
