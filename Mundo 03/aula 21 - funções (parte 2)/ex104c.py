def leiaInt(msg):
    while True:
        try:
        # O try permite que o código dê erro, levando para o except
            num = int(input(msg))
            return num
        # Caso o que estiver dentro do try dê errado, ele executa o que estiver no except
        # Após o except aparece o tipo de erro
        except ValueError:
            print('\033[1;31mERRO. Digite um valor inteiro.\033[m')

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')