extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
           'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
           'Dezoito', 'Dezenove', 'Vinte')

while True:
    numerico = -1
    while numerico > 20 or numerico < 0:
        numerico = int(input('Digite um número: '))
    print(f'Você digitou {extenso[numerico]}')

    continuar = ' '
    while continuar[0] not in 'SsNn':
        continuar = str(input('Deseja continuar? '))
    if continuar[0] in 'Nn':
        break

print('PROGRAMA ENCERRADO')
