lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
# Listas são mutáveis
lanche[3] = 'Picolé'

# Adicionar elementos em listas
lanche.append('Bolo')
lanche.insert(3, 'Chocolate')

# Deletar elementos
del lanche[0]
lanche.pop()             # deleta o último / pode colocar o valor que quiser no ()
if 'Pudim' in lanche:
    lanche.remove('Pudim')

print(lanche)

num = (2,5,9,1)
