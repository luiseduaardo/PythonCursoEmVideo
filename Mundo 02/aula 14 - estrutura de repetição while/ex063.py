'''print('----- SEQUÊNCIA DE FIBONACCI -----')

num = int(input('quantos termos você deseja ver? '))

n1 = 0
n2 = 1
print(f'{n1} - {n2} ', end = '')
cont = 3

while cont <= num:
    n3 = n1 + n2
    print(f'- {n3} ', end = '')
    n1 = n2
    n2 = n3
    cont += 1

print('- FIM')'''

print('----- SEQUÊNCIA DE FIBONACCI 2.0 -----')

num = int(input('quantos termos você deseja ver? '))
seq = 0
adc = 1
cont = 0

while cont <= num:
    print(seq, end = ' - ')
    seq = seq + adc
    adc = seq - adc
    cont += 1

print('FIM')
