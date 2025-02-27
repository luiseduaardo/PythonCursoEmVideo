print('-'*30)
titulo = 'LISTA DE COMPRAS'
print(titulo.center(30))
print('-'*30)

maismil = soma = maisbarP = 0
maisbarN = ''

while True:
    produtoN = str(input('Nome do produto: ')).strip()
    produtoP = float(input('Preço do produto: R$'))

    soma += produtoP

    if produtoP > 1000:
        maismil += 1

    if maisbarP == 0:
        maisbarP = produtoP
        maisbarN = produtoN

    if produtoP < maisbarP:
        maisbarP = produtoP
        maisbarN = produtoN

    print('-' * 30)
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? ')).strip()[0]
    print('-' * 30)

    if continuar in 'Nn':
        break

print('COMPRA FINALIZADA')
print(f'''O total gasto na compra foi de R${soma:.2f}.
Nessa lista, {maismil} produtos custam acima de R$1000.00
O produto mais barato foi {maisbarN}, que custou R${maisbarP:.2f}''')
