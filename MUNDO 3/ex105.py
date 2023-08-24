def notas(*n, sit=False):
    """
    -> ANALISAR NOTAS E SITUAÇÃO.
    :param n: Notas dos alunos (não tem limite).
    :param sit: valor opcional para adicionar ou não a situação do aluno.
    :return: dicionário com as informações dos alunos.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)

    if sit:
        if r['media'] > 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'

    return r


# help(notas)
resp = notas(5.5, 3.5, 9, 7.5)
resp2 = notas(6.5, 7.5, 5, 9, sit=True)
print(f'{resp}, \n{resp2}')
