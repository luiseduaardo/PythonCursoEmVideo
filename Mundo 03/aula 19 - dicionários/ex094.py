geral = list()
individual = dict()
soma = 0

while True:
    individual.clear()
    individual['nome'] = str(input('Nome: ')).strip().title()
    individual['idade'] = int(input('Idade: '))
    while True:
        individual['sexo'] = str(input('Sexo: ')).strip().title()
        if individual['sexo'][0] in 'MF':
            break
        print('ERRO! Por favor digite apenas Masculino ou Feminino.')
    soma += individual['idade']
    geral.append(individual.copy())

    while True:
        cont = str(input('Deseja continuar? ')).strip().title()
        if cont in 'SN':
            break
    if cont[0] in 'N':
        break

print('-=' * 30)

print(f'a) Foram cadastradas {len(geral)} pessoas.')

print(f'b) A média de idade é de {soma/len(geral):.2f} anos de idade.')

print('c) As mulheres nessa lista são: ', end = '')
for c in range(len(geral)):
    if geral[c]['sexo'][0] in 'Ff':
        print(geral[c]['nome'], end = ' ')

print()

print('d) As pessoas com idade acima da média são: ')
for c in range(len(geral)):
    if geral[c]['idade'] > soma/len(geral):
        print(f'{geral[c]['nome']} ({geral[c]['sexo']}), com {geral[c]['idade']}')
