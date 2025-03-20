from utilidadesCev import moeda

p = float(input('Digite o preço: '))
desc = int(input('Quantos % de desconto? '))
aum = int(input('Quantos % de aumento? '))
form = str(input('Deseja mostrar a formatação monetária? ')).strip().title()[0]
if form in 'S':
    form = True
else:
    form = False

print('-' * 30)

print(f'A metade de {moeda.moeda(p, form)} é {moeda.metade(p, form)}')
print(f'O dobro de {moeda.moeda(p, form)} é de {moeda.dobro(p, form)}')
print(f'O preço final após o desconto de {desc}% sobre o valor de {moeda.moeda(p, form)} é de {moeda.diminuir(p, desc, form)}')
print(f'O preço final após o aumento de {aum}% sobre o valor de {moeda.moeda(p, form)} é de {moeda.aumentar(p, aum, form)}')
