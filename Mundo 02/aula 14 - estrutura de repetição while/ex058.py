from random import randint
comp = randint(1, 100)
jog = int(input('Escolha um número de 1 à 100: '))
cont = 1
while jog != comp:
    print('você ERROU! tente novamente com', end = ' ')
    if jog > comp:
        print('um número menor')
    else:
        print('um número maior')
    jog = int(input('Escolha um número de 1 à 100: '))
    cont = cont + 1
print('você ACERTOU!')
print(f'foram necessárias {cont} tentativas')
