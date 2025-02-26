a = float(input('medida do primeiro segmento: '))
b = float(input('medida do segundo segmento: '))
c = float(input('medida do terceiro segmento: '))

if a + b > c and b + c > a and a + c > b:
    print(f'\nesses segmentos \033[1;32mpodem\033[m formar um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif a == b != c or a == c != b or c == b !=a:
        print('ISÓCELES')
    else:
        print('ESCALENO')
else:
    print('\nesses segmentos \033[1;31mnão podem\033[m formar um triângulo')
