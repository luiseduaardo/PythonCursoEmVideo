dis = float(input('qual a distância da sua viagem em km? '))
if dis <= 200:
    print(f'o preço da passagem é de R${dis*0.50:.2f}')
else:
    print(f'o preço da passagem é de R${dis*0.45:.2f}')
