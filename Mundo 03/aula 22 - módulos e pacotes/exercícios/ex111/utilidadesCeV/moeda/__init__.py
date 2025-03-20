def aumentar(n, a, f=False):
    res = (1+(a/100)) * n
    if f:
        return moeda(res)
    return res

def diminuir(n, d, f=False):
    res = (1-(d/100)) * n
    if f:
        return moeda(res)
    return res

def dobro(n, f=False):
    if f:
        return moeda(n*2)
    return n*2

def metade(n, f=False):
    if f:
        return moeda(n/2)
    return n / 2

def moeda(n, moeda = 'R$', f=False):
    return f'{moeda}{n:.2f}'.replace('.', ',')

def resumo(val, desc, aum):
    print('-' * 40)
    print(f'{'RESUMO DO VALOR':^40}')
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(val)}')
    print(f'Metade do preço: \t{metade(val, f = True)}')
    print(f'Dobro do preço: \t{dobro(val, f = True)}')
    print(f'Desconto de {desc}%: \t{diminuir(val, desc, f = True)}')
    print(f'Aumento de {aum}%: \t{aumentar(val, aum, f = True)}')
