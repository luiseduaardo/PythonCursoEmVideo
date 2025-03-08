lista = list()
for c in range(5):
    lista.append(int(input('Digite um número: ')))

print('-'*20)
print(f'Os valores digitados foram: {lista}')
print(f'O maior valor foi {max(lista)}, que está na posição {lista.index(max(lista))}')
print(f'O menor valor foi {min(lista)}, que está na posição {lista.index(min(lista))}')
