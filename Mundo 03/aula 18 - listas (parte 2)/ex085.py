geral = [[], []]

for c in range(7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        if num not in geral[0]:
            geral[0].append(num)
    else:
        if num not in geral[1]:
            geral[1].append(num)

print('-='*30)
print(f'Os valores pares são: {sorted(geral[0])}')
print(f'Os valores ímpares são: {sorted(geral[1])}')
