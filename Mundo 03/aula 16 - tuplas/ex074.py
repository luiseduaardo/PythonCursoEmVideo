from random import randint

n1 = randint(1,100)
n2 = randint(1,100)
n3 = randint(1,100)
n4 = randint(1,100)
n5 = randint(1,100)

tupla = (n1,n2,n3,n4,n5)
ordem = sorted(tupla)

print(f'Fora de ordem: {tupla}')
print(f'Em ordem: {tuple(ordem)}')

# 01
print(f'O maior número dessa tupla é {ordem[len(ordem)-1]} e o menor é {ordem[0]}')

# 02
print(f'O maior número dessa tupla é {max(tupla)} e o menor é {min(tupla)}')