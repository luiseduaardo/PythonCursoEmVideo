tupla = ('Garrafa', 15,
         'Estojo', 8.50,
         'Mochila', 94.35,
         'Caneta', 2,
         'Lápis', 5.60,
         'Borracha', 1.40)

print('-'*45)
print(' '* 14,'LISTA DE PREÇOS', ' '* 14)
print('-'*45)

for c in range (0, len(tupla), 2):
    print(f'{tupla[c]:.<30} R$', end = '')
    print(f'{tupla[c+1]:>7.2f}')

print('-'*45)
