nome = str(input('qual o seu nome? ')).strip().title()
if nome == 'Luís':
    print('que nome bonito!')
elif nome == 'Cláudia' or nome == 'Saulo':
    print('nome legal! só não é melhor que Luís')
elif nome in 'Neném Odete':
    print('gostei do seu nome!')
else:
    print('que nome horrível')
print(f'tenha um bom dia \033[31;1m{nome}')
