tupla = (int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')))

print('-'*15)
print(f'o número 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'o primeiro valor 3 apareceu na posição {tupla.index(3) + 1}')
else:
    print('o número 3 não apareceu nenhuma vez')

print('Os valores pares são: ', end = '')
for c in tupla:
    if c % 2 == 0:
        print(c, end = ' ')

