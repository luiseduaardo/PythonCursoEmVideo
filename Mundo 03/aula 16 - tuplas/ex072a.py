extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
           'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
           'Dezoito', 'Dezenove', 'Vinte')

while True:
    numerico = int(input('Me dê um número de 0 à 20: '))
    if 0 <= numerico <= 20:
        break
    print('TENTE NOVAMENTE')

print(f'Você digitou {extenso[numerico]}')
