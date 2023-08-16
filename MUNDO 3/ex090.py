alunos = {'nome': str(input('Nome: ')), 'media': float(input('Média: ')),
          'situacao': ['Reprovado', 'Recuperação', 'Aprovado']}

print('-=' * 30)
print(f'Nome é igual a {alunos["nome"]}')
print(f'Média é igual a {alunos["media"]}')
print(f'A situação é igual a ', end='')
if alunos['media'] < 5:
    print(alunos['situacao'][0])
elif 5 <= alunos['media'] < 7:
    print(alunos['situacao'][1])
else:
    print(alunos['situacao'][2])
