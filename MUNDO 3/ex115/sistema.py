from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criarArq(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Ver pessoas.
        lerArq(arq)

    elif resposta == 2:
        # Cadastrar pessoas.
        cabecalho('CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        # Sair do sistema
        cabecalho('Saindo do sistema...')
        break
    else:
        print('\033[31mERRO! Opção inválida.\033[m')
    sleep(1.5)
