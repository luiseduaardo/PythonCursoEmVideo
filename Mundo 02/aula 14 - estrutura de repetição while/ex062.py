termo = int(input('digite o primeiro termo: '))
razao = int(input('digite a razão: '))
cont = 1
total = 0
mais = 10

print('os 10 primeiros termos dessa PA são: ', end = '')

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end = ' ➝ ')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('FIM!', end = ' ')
print(f'Foram mostrados {total} termos dessa PA')