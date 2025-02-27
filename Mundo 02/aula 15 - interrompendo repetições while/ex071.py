print('-'*40)
titulo = 'BANCO CEV'
print(titulo.center(40))
print('-'*40)

sacar = int(input('Quanto você deseja sacar? R$'))
valor = sacar
n100 = n50 = n20 = n10 = n5 = n1 = 0

print('-'*40)

while True:
    print(f'Para o valor de R${valor:.2f}, você receberá:')

    if sacar >= 100:
        n100 = sacar // 100
        sacar = sacar % 100
        print(f'{n100} notas de 100 reais')

    if sacar >= 50:
        n50 = sacar // 50
        sacar = sacar % 50
        print(f'{n50} notas de 50 reais')

    if sacar >= 20:
        n20 = sacar // 20
        sacar = sacar % 20
        print(f'{n20} notas de 20 reais')

    if sacar >= 10:
        n10 = sacar // 10
        sacar = sacar % 10
        print(f'{n10} notas de 10 reais')

    if sacar >= 5:
        n5 = sacar // 5
        sacar = sacar % 5
        print(f'{n5} notas de 5 reais')

    if sacar >= 1:
        n1 = sacar
        print(f'{n1} notas de 1 real')

    break

print('-'*40)
