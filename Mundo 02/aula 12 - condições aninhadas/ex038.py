a = int(input('primeiro número: '))
b = int(input('segundo número: '))

if a > b:
    print(f'{a} é maior')
    print(f'{b} é menor')
elif a < b:
    print(f'{a} é menor')
    print(f'{b} é maior')
else:
    print(f'não existe valor maior ou menor. {a} é igual a {b}')
