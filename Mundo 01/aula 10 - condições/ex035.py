a = float(input('quanto vale o primeiro segmento? '))
b = float(input('quanto vale o segundo segmento? '))
c = float(input('quanto vale o terceiro segmento? '))

if a + b > c and b + c > a and a + c > b:
    print('os segmentos PODEM formar um triângulo')
else:
    print('os segmentos NÃO PODEM formar um triângulo')
