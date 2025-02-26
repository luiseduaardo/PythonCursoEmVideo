s = 0
for c in range (1, 7):
    c = int(input(f'{c}° número: '))
    if c % 2 == 0:
        s += c
print(f'a soma dos números pares é de {s}')
