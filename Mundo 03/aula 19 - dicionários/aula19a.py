brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

for c in range(len(brasil)):
    print(f'O {brasil[c]['UF']} tem como sigla {brasil[c]['sigla']}')
