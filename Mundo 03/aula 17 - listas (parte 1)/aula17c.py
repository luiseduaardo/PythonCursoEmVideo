valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

print(f'a lista é: {valores}')
for c, v in enumerate(valores):
    print(f'Na posição {c+1}, encontrei o valor {v}!')
print('Cheguei ao final da lista!')
