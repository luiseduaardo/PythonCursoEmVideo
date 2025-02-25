from random import randint
com = int(input('escolha um número de 0 a 5: '))
escolhido = randint(0, 5)
if com == escolhido:
    print('parabéns, você acertou!')
else:
    print(f'você errou. o número escolhido foi {escolhido}')
