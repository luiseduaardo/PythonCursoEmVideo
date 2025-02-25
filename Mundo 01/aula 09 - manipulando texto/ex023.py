num = int(input('me dê um número de 0 a 9999 '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'analisando o número {num}')
print(f'milhar: {m}')
print(f'centena: {c}')
print(f'dezena: {d}')
print(f'unidade: {u}')