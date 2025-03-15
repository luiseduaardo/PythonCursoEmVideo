aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))

if aluno['media'] < 5:
    aluno['situação'] = 'reprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'em recuperação'
else:
    aluno['situação'] = 'aprovado'

print('-'*30)

print(f'{aluno['nome']} teve média de {aluno['media']:.2f} e está {aluno['situação']}')

print('-'*30)

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
