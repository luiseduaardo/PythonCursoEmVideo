def aumentar(n, a, f=False):
    # Sintaxe 1
    res = (1+(a/100)) * n
    return res if f is False else moeda(res)

def diminuir(n, d, f=False):
    # Sintaxe 2
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

def moeda(n, f=False):
    return f'R${n:.2f}'