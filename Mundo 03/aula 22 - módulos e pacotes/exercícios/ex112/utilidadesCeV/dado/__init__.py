def leiadinheiro(msg):
    while True:
        try:
            inp = input(msg).strip().replace(',', '.')
            inp = float(inp)
            return inp
        except ValueError:
            print(f'\033[1;31mERRO. "{inp}" não é um valor válido.\033[m')
