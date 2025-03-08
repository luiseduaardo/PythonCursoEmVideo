lista = list()
par = list()
impar = list()

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        if num not in par:
            par.append(num)
    else:
        if num not in impar:
            impar.append(num)

    cont = ' '
    while cont[0] not in 'SsNn':
        cont = str(input('Deseja continuar? '))
    if cont[0] in 'Nn':
        break

print('-='*30)
print(f'A lista digitada em ordem foi a seguinte: {sorted(lista)}')
print(f'Os números pares são: {sorted(par)}')
print(f'Os números ímpares são: {sorted(impar)}')
