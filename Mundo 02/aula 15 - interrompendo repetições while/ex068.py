from random import randint
from time import sleep

print('-'*20)
titulo = 'PAR OU ÍMPAR'
print(titulo.center(20))
print('-'*20)

cont = 0

while True:
    # Variáveis relevantes
    jogador = ' '
    while jogador not in 'PI':
        jogador = str(input('Par ou Ímpar? ')).strip().upper()[0]

    numeroJ = int(input('Escolha um número de 0 à 10: '))

    numeroM = randint(0,10)

    soma = numeroJ + numeroM
    paridade = ''

    #Determinando paridade da soma
    if soma % 2 == 0:
        paridade = 'Par'
    else:
        paridade = 'Impar'
    print('-'*20)
    print(f'máquina escolhe {numeroM}. a soma vale {soma}, que é {paridade}')

    #Determinando vitória ou derrota
    if paridade[0] == jogador:
        print('você GANHOU')
        cont += 1

    else:
        print('você PERDEU')
        break

    print('-'*20)

print('-'*20)
print(f'programa ENCERRADO. você obteve {cont} vitórias consecutivas')
