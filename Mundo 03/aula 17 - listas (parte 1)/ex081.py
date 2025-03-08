lista = list()

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    cont = ' '
    while cont not in 'SsNn':
        cont = str(input('Deseja continuar? ')).strip()
    if cont in 'Nn':
        break

print('-='*20)
print(f'A lista é a seguinte: {lista}')
print(f'Foram digitados {len(lista)} valores...')
print(f'Ordem crescente: {sorted(lista)}')
print(f'Ordem decrescente: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 está na lista nas posições ', end = '')
    for indice, valor in enumerate(lista):
        if valor == 5:
            print(f'{indice+1}... ', end = '')

else:
    print('O valor 5 não está na lista')
