num = int(input('Digite um número: '))
fatorial = 1
conta = num

while conta != 0:
    fatorial = conta * fatorial
    conta = conta - 1

print(f'{num}! é {fatorial}')
