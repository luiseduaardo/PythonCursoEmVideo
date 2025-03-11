lista = [[[], [], []], [[], [], []], [[], [], []]]

for i in range(3):
    for j in range(3):
        lista[i][j].insert(j, int(input(f'Digite um valor para a posição [{i}, {j}]: ')))

print('-='*30)
print('A sua matriz 3x3 é a seguinte:')

for i in range(3):
    for j in range(3):
        print(lista[i][j], end = ' ')
    print()
