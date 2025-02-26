num = int(input('me dê um número qualquer: '))
print(f'aqui vai a tabuada do {num}!')
print('-='*10)
for tabuada in range (0, 11):
    print(f'{num} x {tabuada} = {num*tabuada}')
print('FIM')
print('-='*10)
