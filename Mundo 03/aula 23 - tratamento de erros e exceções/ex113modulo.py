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

def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except (ValueError, TypeError):
            print('\033[1;31mERRO. Digite um valor de ponto flutuante.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mEntrada de formatação interrompida pelo usuário\033[m')
            return 0
