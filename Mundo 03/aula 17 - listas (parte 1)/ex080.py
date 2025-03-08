from time import sleep
lista = list()

for c in range(5):
    n = int(input('Digite um valor: '))

# Se o valor for o primeiro digitado ou for maior do que o que já era maior anteriormente
    if c == 0:
        lista.append(n)
        print('Lista iniciada...')

    elif n > lista[len(lista)-1]:
        lista.append(n)
        print('Valor adicionado no final da lista...')

    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                break
            posicao += 1
        print(f'Valor adicionado na posição {posicao+1}...')

print('')
sleep(0.5)
print('LISTA ENCERRADA. PROCESSANDO A LISTA...')
sleep(1.5)

print('')
print(f'Os valores digitados em ordem foram {lista}')
