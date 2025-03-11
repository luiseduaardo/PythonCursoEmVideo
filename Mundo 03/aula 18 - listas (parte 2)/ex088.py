from random import randint

jogos = int(input('Quantos jogos você deseja fazer? '))
todos = []

for c in range(jogos):
    indiv = []
    for j in range(6):
        while True:
            num = randint(1,60)
            if num not in indiv:
                indiv.append(num)
                break
    indiv.sort()
    todos.append(indiv)

print('-='*30)
print('Sugiro os seguintes jogos:')
for c in range(jogos):
    print(f'{c+1}. {todos[c]}')
