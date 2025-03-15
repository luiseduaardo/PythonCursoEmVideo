from random import randint
from time import sleep
from operator import itemgetter

dici = dict()

qntd = int(input('Quantos jogadores vão jogar? '))

for c in range(qntd):
    dici[f'jogador {c+1}'] = randint(1,6)

for k, v in dici.items():
    print(f'{k} tirou {v}')
    sleep(1)

ranking = sorted(dici.items(), key = itemgetter(1), reverse = True)

print('-' * 40)

print('=== RANKING DOS JOGADORES ===')

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]} pontos')
    sleep(1)
