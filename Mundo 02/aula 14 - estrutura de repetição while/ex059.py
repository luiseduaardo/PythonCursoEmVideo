priVal = int(input('Primeiro valor: '))
segVal = int(input('Segundo valor: '))
info = 0

while info != 5:
    print('''    [ 1 ] Soma
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    info = int(input('Selecione a opção que você deseja: '))
    print('-='*20)

    if info == 1:
            print(f'A soma entre {priVal} e {segVal} é de {priVal + segVal}')

    elif info == 2:
            print(f'O produto entre {priVal} e {segVal} é de {priVal*segVal}')

    elif info == 3:
        if priVal > segVal:
             print(f'{priVal} é maior que {segVal}')
        elif priVal < segVal:
            print(f'{segVal} é maior que {priVal}')
        else:
            print(f'{priVal} e {segVal} são iguais')

    elif info == 4:
        priVal = int(input('Primeiro valor: '))
        segVal = int(input('Segundo valor: '))

    elif info > 5:
        print('opção inválida. TENTE NOVAMENTE')
    print('-='*20)

print('\nMENU ENCERRADO')
