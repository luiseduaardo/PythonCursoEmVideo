# Regras de fatiamento de strings funcionam para tuplas

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

print(lanche)

# Posição na tupla não é necessária
for comida in lanche:
    print(comida, end =', ')

#Caso seja necessária a posição na tupla
for cont in range (0, len(lanche)):
    print(f'\n{lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'{comida} na posição {pos}')

# Dá a tupla organizada em ordem alfabética, transformando a tupla () em uma LISTA []
print(sorted(lanche))