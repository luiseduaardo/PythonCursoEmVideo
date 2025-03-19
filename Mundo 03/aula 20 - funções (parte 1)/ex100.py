from random import randint
from time import sleep

def sorteia(lista):
    print('Foram sorteados os seguintes valores: ', end = '')
    for c in range(5):
        sleep(0.5)
        valor = randint(0,10)
        lista.append(valor)
        print(valor, end = ' | ')
    print()

def somapar(lista):
    soma = 0
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            soma += v
    print(f'A soma entre os pares dessa lista é de {soma}')

numeros = list()
sorteia(numeros)
somapar(numeros)
