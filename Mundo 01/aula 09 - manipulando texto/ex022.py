nomecompleto = str(input('qual o seu nome completo? ')).strip()
nomeupper = nomecompleto.upper()
nomelower = nomecompleto.lower()
dividido = nomecompleto.split()
letras = len(''.join(dividido))
primeiro = len(dividido[0])

print(f'''seu nome completo em diferentes versões: \n
maiúsculo: {nomeupper}
minúsculo: {nomelower}
total de letras sem espaços: {letras}
letras no primeiro nome: {primeiro}''')