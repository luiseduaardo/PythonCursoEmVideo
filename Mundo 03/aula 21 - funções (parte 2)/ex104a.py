def leia(msg):
    while True:
        num = str(input(msg))
        if num.lstrip('-').isnumeric():
            return int(num)
        else:
            print('\033[1;31mERRO. Digite um valor inteiro.\033[m')


n = leia('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
