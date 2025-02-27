while True:
    num = int(input('Digite um número qualquer: '))
    if num < 0:
        break
    for tabuada in range (11):
        print(f'{num} x {tabuada} = {num*tabuada}')
    print('~'*15)

print('PROGRAMA ENCERRADO')
