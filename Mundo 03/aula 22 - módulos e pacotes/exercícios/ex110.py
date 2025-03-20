from utilidadesCev import moeda

p = float(input('Digite o preço: '))
desc = int(input('Quantos % de desconto? '))
aum = int(input('Quantos % de aumento? '))

moeda.resumo(p, desc, aum)
