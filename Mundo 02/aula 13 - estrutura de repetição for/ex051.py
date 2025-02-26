print('CALCULADORA DE PA')
prim = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = prim + (9*raz)

for pa in range (prim, dec + raz, raz):
    print(pa, end = ' → ')

'''s = prim
print('\nos 10 primeiros termos dessa PA são:')
for pa in range (1, 11):
    print(f'{s}', end = ' → ')
    s += raz
print('fim')'''
