num = som = cont = 0

print('DIGITE 999 PARA PARAR')

while True:                                  # Loop infinito
    num = int(input('Digite um número: '))
    # Caso 999 (flag) seja digitado, o programa é encerrado, sem adicionar no contador nem na soma
    if num == 999:
        break
    som += num
    cont += 1

print(f'Foram digitados {cont} números e a soma entre eles é de {som}')
print('PAROU')
