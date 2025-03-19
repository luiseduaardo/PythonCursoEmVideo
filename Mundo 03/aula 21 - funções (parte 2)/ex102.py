def fatorial(num, show=False):
    '''
    :param num: Mostra o número a ser calculado
    :param show: Caso seja verdadeiro, mostra a conta
    :return: Resultado do fatorial de num
    '''
    from time import sleep
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end = '')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
            sleep(0.5)
        f *= c
    return f

n = int(input('Qual valor você deseja ver o fatorial? '))
p = str(input('Deseja ver o processo? ')).strip().title()[0]
print('-' * 30)
print(f'O valor de {n}! é {fatorial(n)}')
if p == 'S':
    print(fatorial(n, show=True))
