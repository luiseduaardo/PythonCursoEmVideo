def leia(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[1;31mERRO. Digite um valor inteiro.\033[m')
        if ok:
            break
    return valor

n = leia('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
