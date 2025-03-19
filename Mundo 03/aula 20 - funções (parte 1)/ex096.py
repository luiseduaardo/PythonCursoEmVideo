def area(larg, comp):
    ar = larg*comp
    print(f'A área do seu terreno de {larg}m x {comp}m é {ar:.2f}m²')

print('-'*30)
print(f'{'CONTROLE DE TERRENOS':^30}')
print('-'*30)

l = float(input('Qual a largura do seu terreno? '))
c = float(input('Qual o comprimento do seu terreno? '))
area(l, c)
