def ficha(jogador = '<desconhecido>', gols = 0):
    '''
    :param jogador: Nome do jogador
    :param gols: Quantos gols o jogador fez
    :return: Nome e gols
    '''
    print('-' * 40)
    return f'O jogador {jogador} fez {gols} gols.'

n = str(input('Nome: ')).strip().title()
g = str(input('Gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    print(ficha(gols=g))
else:
    print(ficha(n, g))
