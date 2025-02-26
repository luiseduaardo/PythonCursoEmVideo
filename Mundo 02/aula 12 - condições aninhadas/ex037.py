print('-='*20)
print('CONVERSOR DE BASES NÚMERICAS')
print('-='*20)
num = int(input('me dê um número qualquer '))
print('\nescolha uma das bases para converter:')
print('[ 1 ] converter em BINÁRIO')
print('[ 2 ] converter em OCTAL')
print('[ 3 ] converter em HEXADECIMAL')
escolha = int(input('qual será a base de conversão? '))

if escolha == 1:
    print(f'o número {num} em BINÁRIO equivale a \033[31m{bin(num)[2:]}\033[m')
elif escolha == 2:
    print(f'o número {num} em OCTAL  equivale a \033[31m{oct(num)[2:]}\033[m')
elif escolha == 3:
    print(f'o número {num} em HEXADECIMAL equivale a \033[31m{hex(num)[2:]}\033[m')
else:
    print('\033[1;7;31mescolha uma base válida\033[m')
