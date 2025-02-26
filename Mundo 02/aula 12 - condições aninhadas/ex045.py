from random import choice
from time import sleep
escolha = str(input('vamos jogar jokenpô! ')).strip().title()
maquina = choice(['Pedra', 'Papel', 'Tesoura'])
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!!')
if escolha == maquina:
    print(f'\033[1;33mEMPATE\033[m! nós dois escolhemos {escolha.upper()}')
else:
    if maquina == 'Pedra': # Computador joga PEDRA
        if escolha == 'Papel':
            print('você \033[1;32mGANHOU\033[m! eu escolhi PEDRA')
        elif escolha == 'Tesoura':
            print('você \033[1;31mPERDEU\033[m! eu escolhi PEDRA')
    elif maquina == 'Papel': #Computador joga PAPEL
        if escolha == 'Pedra':
            print('você \033[1;31mPERDEU\033[m! eu escolhi PAPEL')
        elif escolha == 'Tesoura':
            print('você \033[1;32mGANHOU\033[m! eu escolhi PAPEL')
    elif maquina == 'Tesoura': #Computador joga TESOURA
        if escolha == 'Papel':
            print('você \033[1;31mPERDEU\033[m! eu escolhi TESOURA')
        elif escolha == 'Pedra':
            print('você \033[1;32mGANHOU\033[m eu escolhi TESOURA')
