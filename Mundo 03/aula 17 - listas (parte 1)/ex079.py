lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor já digitado.')
    else:
        lista.append(valor)
        print('Novo valor adicionado.')

    cont = str(input('Deseja continuar? ')).strip()
    if cont[0] in 'Nn':
        break

lista.sort()
print(f'Os valores digitados foram: {lista}')
