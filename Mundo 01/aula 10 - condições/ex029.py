v = float(input('qual a velocidade do carro em km/h? '))
multa = (v-80)*7
if v <= 80:
    print('você está na velocidade correta!')
else:
    print(f'você ultrapassou o limite de velocidade. a sua multa é de: R${multa:.2f}')