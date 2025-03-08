lista = list()
par = list()
impar = list()

while True:
    lista.append(int(input('Digite um número: ')))
    cont = ' '
    while cont[0] not in 'SsNn':
        cont = str(input('Deseja continuar? '))
    if cont[0] in 'Nn':
        break

for indice, valor in enumerate(lista):
    if valor % 2 == 0:
        if valor not in par:
            par.append(valor)
    else:
        if valor not in impar:
            impar.append(valor)

print('-='*30)
print(f'A lista digitada em ordem foi a seguinte: {sorted(lista)}')
print(f'Os números pares são: {sorted(par)}')
print(f'Os números ímpares são: {sorted(impar)}')