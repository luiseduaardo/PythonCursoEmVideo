#from math import sqrt, pow
#c1 = float(input('me dê um valor para o primeiro lado do triângulo retângulo '))
#c2 = float(input('me dê um valor para o outro lado desse triângulo retângulo '))
#h = sqrt(pow(c1, 2)+pow(c2, 2))
#print(f'a hipotenusa em um triângulo com catetos valendo {c1} e {c2} vale {h}')

from math import hypot
c1 = float(input('me dê um valor para o primeiro lado do triângulo retângulo '))
c2 = float(input('me dê um valor para o outro lado desse triângulo retângulo '))
h = hypot(c1, c2)
print(f'a hipotenusa em um triângulo com catetos valendo {c1} e {c2} vale {h}')

#c1 = float(input('me dê um valor para o primeiro lado do triângulo retângulo '))
#c2 = float(input('me dê um valor para o outro lado desse triângulo retângulo '))
#h = (c1**2+c2**2)**(1/2)
#print(f'a hipotenusa em um triângulo com catetos valendo {c1} e {c2} vale {h}')