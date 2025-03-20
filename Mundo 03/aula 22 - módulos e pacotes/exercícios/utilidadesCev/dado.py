def val(msg):
    while True:
        try:
            inp = input(msg).strip()
            inp = float(inp)
            return inp
        except ValueError:
            print(f'\033[1;31mERRO. Digite um valor válido.\033[m')
