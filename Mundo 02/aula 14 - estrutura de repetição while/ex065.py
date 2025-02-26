maiorV = menorV = soma = cont = 0
continuar = 'S'

while continuar in 'Ss':
    val = int(input('Digite um valor: '))
    soma += val
    cont += 1
    if cont == 0:
        maiorV = menorV = val
    if val > maiorV:
        maiorV = val
    if val < menorV:
        menorV = val
    continuar = str(input('Deseja digitar um número? ')).strip().upper()[0]

print(f'A média entre os números digitados é de {soma/cont}.')
print(f'O maior número digitado é {maiorV} e o menor é {menorV}')
