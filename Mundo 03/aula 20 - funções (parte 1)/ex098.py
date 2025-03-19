from time import sleep
def contador(inicio, fim, passo):
    print('-' * 30)
    print(f'Iniciando contagem de {inicio} até {fim} de {passo} em {passo}')
    cont = inicio
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio > fim:
        while cont >= fim:
            print(f'{cont}', end = ' | ')
            sleep(0.5)
            cont -= passo
        print()
    if inicio < fim:
        while cont <= fim:
            print(f'{cont}', end = ' | ')
            sleep(0.5)
            cont += passo
        print()

contador(1, 10, 1)
contador(10, 0, 2)

print('-' * 30)
print(f'{'AGORA É A SUA VEZ':^30}')
print('-' * 30)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
