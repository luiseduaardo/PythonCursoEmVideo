def linha(tam=50):
    return '-' * tam


def titulo(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(*lista):
    titulo('MENU PRINCIPAL')
    for i, v in enumerate(lista, start=1):
        print(f'{i} - {v}')
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc


def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except (ValueError, TypeError):
            print('\033[1;31mERRO. Digite um valor inteiro.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mEntrada de formatação interrompida pelo usuário\033[m')
            return 0
