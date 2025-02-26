preco = float(input('qual o preço do produto que você deseja comprar? R$'))
modalidade = int(input('''escolha uma modalidade de pagamento:
[ 1 ] à vista
[ 2 ] à vista no cartão
[ 3 ] em 2x no cartão
[ 4 ] em 3x ou mais no cartão
selecione a forma de pagamento: '''))

if modalidade == 1:
    print(f'o valor a ser pago é de R${preco*0.9:.2f}')
elif modalidade == 2:
    print(f'o valor a ser pago é de R${preco*0.95:.2f}')
elif modalidade == 3:
        print(f'o valor a ser pago é de R${preco:.2f}. o valor da sua parcela é de R${preco/2:.2f}')
elif modalidade == 4:
    parcelas = int(input('em quantas parcelas você irá pagar? '))
    if parcelas < 3:
        print('\033[31mnúmero de parcelas inválido\033[m. tente novamente.')
    else:
        print(f'o valor a ser pago é de R${preco*1.2:.2f}. o valor das suas parcelas são de R${(preco*1.2)/parcelas:.2f}')
else:
    print('\033[31mopção inválida de pagamento. tente novamente.\033[m')
