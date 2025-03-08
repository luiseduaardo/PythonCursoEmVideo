lista = list()
maior = menor = 0

for c in range(5):
    lista.append(int(input('Digite um número: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print('-'*20)
print(f'Os valores digitados foram: {lista}')

print(f'O maior valor digitado foi {maior} nas posições ', end = '')
for indice, valor in enumerate(lista):
    if valor == maior:
        print(f'{indice+1}... ', end = '')
print()

print(f'O menor valor digitado foi {menor} nas posições ', end = '')
for indice, valor in enumerate(lista):
    if valor == menor:
        print(f'{indice+1}... ', end = '')
print()
