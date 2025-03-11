indiv = []
geral = []

while True:
    indiv.append(str(input('Qual o seu nome? ')).strip().title())
    indiv.append(float(input('Qual o seu peso? ')))

    geral.append(indiv[:])
    indiv.clear()

    continuar = ' '
    while continuar[0] not in 'SsNn':
        continuar = str(input('Deseja continuar? '))
    if continuar[0] in 'Nn':
        break

pesada = []
leve = []
maiorP = menorP = geral[0][1]
for a in range(len(geral)):
    if geral[a][1] >= maiorP:
        maiorP = geral[a][1]
    if geral[a][1] <= menorP:
        menorP = geral[a][1]

for b in range(len(geral)):
    if geral[b][1] == maiorP:
        pesada.append(geral[b][0])
    elif geral[b][1] == menorP:
        leve.append(geral[b][0])

print('-='*30)
print(f'Foram analisadas {len(geral)} pessoas')
print(f'O maior peso foi de {maiorP}. Peso de {pesada}')
print(f'O menor peso foi de {menorP}. Peso de {leve}')
