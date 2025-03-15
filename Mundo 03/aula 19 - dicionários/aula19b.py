estado = dict()
brasil = list()

for c in range(3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
    estado.clear()

for e in brasil:
    for k, v in e.items():
     print(f'O campo {k} tem valor {v}')
