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