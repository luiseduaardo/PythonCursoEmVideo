from utilidadesCev import moeda, dado

p = dado.val('Digite o preço: R$')
desc = int(input('Quantos % de desconto? '))
aum = int(input('Quantos % de aumento? '))

moeda.resumo(p, desc, aum)
