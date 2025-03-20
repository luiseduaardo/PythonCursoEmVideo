import moeda3

p = float(input('Digite o preço: '))
desc = int(input('Quantos % de desconto? '))
aum = int(input('Quantos % de aumento? '))
form = str(input('Deseja mostrar a formatação monetária? ')).strip().title()[0]
if form in 'S':
    form = True
else:
    form = False

print('-' * 30)

print(f'A metade de {moeda3.moeda(p, form)} é {moeda3.metade(p, form)}')
print(f'O dobro de {moeda3.moeda(p, form)} é de {moeda3.dobro(p, form)}')
print(f'O preço final após o desconto de {desc}% sobre o valor de {moeda3.moeda(p, form)} é de {moeda3.diminuir(p, desc, form)}')
print(f'O preço final após o aumento de {aum}% sobre o valor de {moeda3.moeda(p, form)} é de {moeda3.aumentar(p, aum, form)}')
