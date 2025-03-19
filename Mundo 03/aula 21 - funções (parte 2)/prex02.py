def paridade(num = 0):
    if num % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'

n = int(input('Digite um valor: '))
print(f'{n} é um número {paridade(n)}')
