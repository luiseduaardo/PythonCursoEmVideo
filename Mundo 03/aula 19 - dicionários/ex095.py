todos = list()
indiv = dict()

while True:
    indiv.clear()
    indiv['nome'] = str(input('Nome: ')).strip().title()
    indiv['partidas'] = int(input(f'Quantas partidas {indiv['nome']} jogou? '))
    indiv['gols'] = list()
    indiv['todos'] = 0
    for c in range(indiv['partidas']):
        indiv['gols'].append(int(input(f'    - Quantos gols na partida {c+1}? ')))
        indiv['todos'] += indiv['gols'][c]
    todos.append(indiv.copy())

    while True:
        cont = str(input('Deseja continuar? ')).strip().title()
        if cont[0] in 'SN':
            break
        print('ERRO! Digite apenas SIM ou NÃO.')
    if cont[0] in 'N':
        break

print('-=' * 30)

print('cod', end = '  ')
for i in indiv.keys():
    print(f'{i:<15}', end = '')
print()

print('-' * 60)

for c in range(len(todos)):
    print(f'{c}   {todos[c]['nome']:<15}{todos[c]['partidas']:<15}{f'{todos[c]['gols']}':<15}{todos[c]['todos']:<20}')

print('-' * 60)

while True:
    jog = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if jog >= len(todos):
        print('ESCOLHA UM NÚMERO VÁLIDO.')
    if jog == 999:
        print('ENCERRANDO.')
        break
    if jog < len(todos):
        print(f'Levantamento de {todos[jog]['nome']}')
        for i, v in enumerate(todos[jog]['gols']):
            print(f'    - Na partida {i+1} fez {v} gols;')
        print(f'Fez um total de {todos[jog]['todos']} gols em {todos[jog]['partidas']} partidas')
