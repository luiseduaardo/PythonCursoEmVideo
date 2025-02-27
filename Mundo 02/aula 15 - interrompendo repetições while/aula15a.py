n = cont = 0

# Interrompe se o n digitado for igual a 999 ou quando o contador chegar a 3
# O primeiro evento que acontece interrompe o programa

while n != 999:
    n = int(input('Digite um número: '))
    cont += 1
    if cont == 5:
        break

print('PAROU')
