from utilidadesCev import moeda

p = float(input('Digite o preço: '))
desc = int(input('Quantos % de desconto? '))
aum = int(input('Quantos % de aumento? '))

print('-' * 30)

print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é de {moeda.moeda(moeda.dobro(p))}')
print(f'O preço final após o desconto de {desc}% sobre o valor de {moeda.moeda(p)} é de {moeda.moeda(moeda.diminuir(p, desc))}')
print(f'O preço final após o aumento de {aum}% sobre o valor de {moeda.moeda(p)} é de {moeda.moeda(moeda.aumentar(p, aum))}')
