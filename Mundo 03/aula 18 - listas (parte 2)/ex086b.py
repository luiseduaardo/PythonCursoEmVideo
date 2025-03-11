lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        lista[i][j] = int(input(f'Digite um valor para a posição [{i}, {j}]: '))

print('-='*30)
print('A sua matriz 3x3 é a seguinte:')

for i in range(3):
    for j in range(3):
        print(f'[{lista[i][j]:^4}]', end = ' ')
    print()
