times = ['Corinthians', 'Atlético-MG', 'Grêmio', 'São Paulo', 'Internacional', 'Sport',
         'Santos', 'Cruzeiro', 'Palmeiras', 'Atlético-PR', 'Ponte Preta', 'Flamengo', 'Fluminense',
         'Chapecoense', 'Coritiba', 'Figueirense', 'Avaí', 'Vasco da Gama', 'Goiás', 'Joinville']

print('=' * 20)
print('BRASILEIRÃO 2015')
print('=' * 20)

# a) Os 5 primeiros colocados
print(f'Os 5 primeiros colocados são: {times[0:5]}')

# b) Os 4 últimos colocados
print(f'\nOs 4 últimos times são {times[-4:]}')

# c) Times em ordem alfabética
print(f'\nA ordem alfabética dos times é a seguinte: {sorted(times)}')

# d) Posição da Chapecoense
print(f'\nA Chapecoense está em {times.index('Chapecoense')+1}° lugar')
