from math import sin, cos, tan, radians
angulo = float(input('me dê um ângulo qualquer em graus '))
rad = radians(angulo)
sen = sin(rad)
cos = cos(rad)
tan = tan(rad)
print(f'o valor do ângulo de {angulo:.2f}° equivale a {rad:.2f} radianos\n seno: {sen:.2f}\n cosseno: {cos:.2f}\n tangente: {tan:.2f}')

