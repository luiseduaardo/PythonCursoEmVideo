import moeda2

p = float(input('Digite o preço: '))
desc = int(input('Quantos % de desconto? '))
aum = int(input('Quantos % de aumento? '))

print('-' * 30)

print(f'A metade de {moeda2.moeda(p)} é {moeda2.moeda(moeda2.metade(p))}')
print(f'O dobro de {moeda2.moeda(p)} é de {moeda2.moeda(moeda2.dobro(p))}')
print(f'O preço final após o desconto de {desc}% sobre o valor de {moeda2.moeda(p)} é de {moeda2.moeda(moeda2.diminuir(p, desc))}')
print(f'O preço final após o aumento de {aum}% sobre o valor de {moeda2.moeda(p)} é de {moeda2.moeda(moeda2.aumentar(p, aum))}')
