# Nesse caso, nem todos os dados são salvos, somente os dos maiores e menores valores
# Para salvar todos os dados, basta criar uma variável chamada geral e dar um geral.append(indiv[:]) antes do indiv.clear()
# Fazendo isso, os valores ficam salvos, mesmo que não estejam sendo usados

indiv = []
maiorP = menorP = contador = 0
maiorN = []
menorN = []

while True:
    indiv.append(str(input('Qual o seu nome? ')).strip().title())
    indiv.append(float(input('Qual o seu peso? ')))

    if contador == 0:
        maiorP = indiv[1]
        menorP = indiv[1]
    else:
        if indiv[1] >= maiorP:
            maiorP = indiv[1]
            maiorN.append(indiv[0])
        if indiv[1] <= menorP:
            menorP = indiv[1]
            menorN.append(indiv[0])

    contador += 1
    indiv.clear()

    continuar = ' '
    while continuar[0] not in 'SsNn':
        continuar = str(input('Deseja continuar? ')).strip()
    if continuar[0] in 'Nn':
        break

print('-='*30)
print(f'Ao todo, você cadastrou {contador} pessoas')

print(f'O maior peso foi de {maiorP}kg, peso de ', end = '')
for numeros, maiores in enumerate(maiorN):
    print(f'{maiores}', end = ' | ')

print()

print(f'O menor peso foi de {menorP}kg, peso de ', end = '')
for numero, menores in enumerate(menorN):
    print(f'{menores}', end = ' | ')
