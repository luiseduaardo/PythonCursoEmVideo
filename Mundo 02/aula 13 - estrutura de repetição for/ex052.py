num = int(input('me dê um número qualquer: '))
tot = 0
for c in range (1, num+1):
    if num % c == 0:
        print('\033[32m', end = ' ')
        tot += 1
    else:
        print('\033[31m', end = ' ')
    print(c, end = ' ')
print(f'\n\033[mo número {num} foi divisível {tot} vezes')
if tot == 2:
    print(f'por isso, {num} é PRIMO')
else:
    print(f'por isso, {num} NÃO É PRIMO')
