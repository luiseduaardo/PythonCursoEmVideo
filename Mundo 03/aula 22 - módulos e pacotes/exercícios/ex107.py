from utilidadesCev import moeda

p = float(input('Digite o preço: '))
desc = int(input('Quantos % de desconto? '))
aum = int(input('Quantos % de aumento? '))

print('-' * 30)

print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é de {moeda.dobro(p)}')
print(f'O preço final após o desconto de {desc}% sobre o valor de {p} é de {moeda.diminuir(p, desc)}')
print(f'O preço final após o aumento de {aum}% sobre o valor de {p} é de {moeda.aumentar(p, aum)}')
