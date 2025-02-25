#tempo = int(input('quantos anos tem o seu carro? '))
#print('carro novo' if tempo <=3 else 'carro velho')
#if tempo <=3:
#    print('carro novo')
#else:
#    print('carro velho')

#nome = str(input('qual o seu nome? ')).title().strip()
#if nome[:4] == 'Luís':
#    print('belo nome')
#else:
#    print('nome horrível')
#print(f'bom dia, {nome}!')

n1 = float(input('digite a sua primeira nota: '))
n2 = float(input('digite a sua segunda nota: '))
media = (n1+n2)/2
print(f'a sua média foi de {media:.2f}')
if media <=6:
    print('infelizmente você foi reprovado')
else:
    print('parabéns! você foi aprovado!')