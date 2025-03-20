def aumentar(n, a, f=False):
    if f:
        return moeda((1+(a/100))*n)
    return (1+(a/100)) * n

def diminuir(n, d, f=False):
    if f:
        return moeda((1-(d/100))*n)
    return (1-(d/100)) * n

def dobro(n, f=False):
    if f:
        return moeda(n*2)
    return n*2

def metade(n, f=False):
    if f:
        return moeda(n/2)
    return n / 2

def moeda(n, f=False):
    return f'R${n:.2f}'

def resumo(val, desc, aum):
    print('-' * 40)
    print(f'{'RESUMO DO VALOR':^40}')
    print('-' * 40)
    print('Preço analisado:', f'{moeda(val):>18}')
    print('Metade do preço:', f'{moeda(metade(val)):>18}')
    print('Dobro do preço:', f'{moeda(dobro(val)):>19}')
    print(f'Desconto de {desc}%:', f'{moeda(diminuir(val, desc)):>18}')
    print(f'Aumento de {aum}%:', f'{moeda(aumentar(val, aum)):>19}')
