cont = som = 0

num = int(input('Me dê um número: '))
while num != 999:
    som += num
    cont += 1
    num = int(input('Me dê um número: '))

print(f'Você digitou {cont} números e a soma entre eles é {som}')
