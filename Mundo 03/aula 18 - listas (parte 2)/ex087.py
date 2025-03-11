lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = somaTerc = maiorSeg = 0

for i in range(3):
    for j in range(3):
        lista[i][j] = int(input('Digite um valor: '))
        # Soma dos pares
        if lista[i][j] % 2 == 0:
            somaPar += lista[i][j]
        # Soma dos valores da terceira coluna
        somaTerc += lista[i][2]
        # Descobrir maior valor da segunda linha
        if j == 0 or lista[1][j] > maiorSeg:
            maiorSeg = lista[1][j]

print('-='*30)
print('A matriz digitada foi a seguinte:')
for i in range(3):
    for j in range(3):
        print(f'[{lista[i][j]:^5}]', end = ' ')
    print()
print('-='*30)
print(f'A soma de todos os valores pares é de {somaPar}')
print(f'A soma de todos os valores da terceira coluna é {somaTerc}')
print(f'O maior valor da segunda linha é {maiorSeg}')
