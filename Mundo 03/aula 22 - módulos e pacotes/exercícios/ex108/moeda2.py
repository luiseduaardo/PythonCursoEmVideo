def aumentar(n, a):
    return (1+(a/100)) * n

def diminuir(n, d):
    return (1-(d/100)) * n

def dobro(n):
    return 2 * n

def metade(n):
    return n / 2

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
