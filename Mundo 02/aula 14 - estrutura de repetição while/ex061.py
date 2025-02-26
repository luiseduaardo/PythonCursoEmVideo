termo = int(input('digite o primeiro termo: '))
razao = int(input('digite a razão: '))
cont = 1

print('os 10 primeiros termos dessa PA são: ', end = '')

while cont <= 10:
    print(f'{termo}', end = ' ➝ ')
    termo = termo + razao
    cont = cont + 1

print('FIM')
