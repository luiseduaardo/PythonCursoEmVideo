nome = str(input('qual o seu nome? ')).strip().title()
sexo = str(input('qual o seu sexo [M/F]? ')). upper().strip()[0]
while sexo not in 'FfMm':
    print('não foi possível salver seu resultado. tente novamente')
    sexo = str(input('qual o seu sexo [M/F]? ')).upper().strip()[0]
print(f'''{nome} - sexo {sexo}
obrigado! suas informações foram salvas.''')
