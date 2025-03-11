# Nesse aprimoramento do exercício 089, foram adicionadas as opções de escolher a ordem alfabética ou de nota no boletim

todos = []
cont = 0

while True:
    individual = []
    nome = str(input('Nome: ')).strip().title()                 # 0 - nome
    individual.append(nome)
    n1 = float(input('1ª nota: '))                              # 1 - nota 1
    individual.append(n1)
    n2 = float(input('2ª nota: '))                              # 2 - nota 2
    individual.append(n2)
    media = (n1+n2)/2                                           # 3 - média
    individual.append(media)
    todos.append(individual[:])
    individual.clear()

    continuar = ' '
    while continuar[0] not in 'SsNn':
        continuar = str(input('Deseja continuar? '))
    if continuar[0] in 'Nn':
        break

print('-=' * 20)

ordem = ' '
while ordem not in 'NnAa':
    ordem = str(input('Deseja ver em ordem alfabética ou de nota? ')).strip().title()
if ordem[0] == 'N':
    todos.sort(key=lambda x: x[3], reverse=True)
if ordem[0] == 'A':
    todos.sort(key=lambda x: x[0])

print('-=' * 20)

print(f'{'No.':<5}{'Nome':<20}{'Média':>8}')

print('-' * 40)

for c in range(len(todos)):
    print(f'{c:<5}'f'{todos[c][0]:<20}'f'{todos[c][3]:>8.2f}')

print('-' * 40)
while True:
    nota = int(input('Mostrar nota de qual aluno? (999 para parar) '))
    if nota <= (len(todos) - 1):
        print(f'As notas obtidas por {todos[nota][0]} foram:')
        print(f'Nota 1: {todos[nota][1]}')
        print(f'Nota 2: {todos[nota][2]}')
    elif nota == 999:
        break
    print('-' * 40)
