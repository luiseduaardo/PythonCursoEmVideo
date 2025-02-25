nome = str(input('qual o seu nome completo? ')).strip().title()
dividido = nome.split()
print(f'seja bem vindo(a) {dividido[0]} {dividido[len(dividido)-1]}')