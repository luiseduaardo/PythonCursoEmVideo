ano = int(input('em que ano você nasceu? '))
idade = 2025-ano

if idade > 18:
    print(f'você \033[1;31mjá passou\033[m do tempo de alistamento há \033[4m{idade-18} anos\033[m')
elif idade < 18:
    print(f'''você \033[33mainda não está na idade\033[m para se alistar. 
    faltam \033[4m{18-idade} anos\033[m para o seu alistamento''')
else:
    print(f'\033[1;32mestá na hora de você se alistar!\033[m')
