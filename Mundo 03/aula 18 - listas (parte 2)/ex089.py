geral = []

while True:
    individual = ['', [0, 0]]
    individual[0] = str(input('Nome: ')).strip().title()
    individual[1][0] = float(input('1ª nota: '))
    individual[1][1] = float(input('2ª nota: '))

    geral.append(individual[:])
    individual.clear()

    continuar = ' '
    while continuar[0] not in 'SsNn':
        continuar = str(input('Deseja continuar? '))
    if continuar[0] in 'Nn':
        break

print('-=' * 20)

print(f'{'No.':<5}{'Nome':<20}{'Média':>8}')

print('-' * 40)

for c in range(len(geral)):
    media = (geral[c][1][0] + geral[c][1][1]) / 2
    print(f'{c:<5}{geral[c][0]:<20}{media:>8.2f}')

print('-'*40)
while True:
    nota = int(input('Mostrar nota de qual aluno? (999 para parar) '))
    if nota <= (len(geral) - 1):
        print(f'As notas obtidas por {geral[nota][0]} foram:')
        print(f'Nota 1: {geral[nota][1][0]}')
        print(f'Nota 2: {geral[nota][1][1]}')
    elif nota == 999:
        break
    print('-'*40)
