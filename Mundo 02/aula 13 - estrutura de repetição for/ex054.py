from datetime import date
menor = 0
maior = 0

for pessoa in range (1, 8):
    ano = int(input(f'ano que a {pessoa}° pessoa nasceu: '))
    if date.today().year - ano >= 18:
        maior += 1
    else:
        menor += 1
print(f'nessa lista existem {menor} pessoas menores de idade e {maior} pessoas maiores de idade')
