#from random import choices
#a1 = input('me dê o nome do primeiro aluno ')
#a2 = input('me dê o nome do segundo aluno ')
#a3 = input('me dê o nome do terceiro aluno ')
#a4 = input('me dê o nome do quarto aluno ')
#print(f'a ordem escolhida foi: {choices([f'{a1}', f'{a2}', f'{a3}', f'{a4}'], k=4)}')

from random import shuffle
a1 = str(input('me dê o nome do primeiro aluno '))
a2 = str(input('me dê o nome do segundo aluno '))
a3 = str(input('me dê o nome do terceiro aluno '))
a4 = str(input('me dê o nome do quarto aluno '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('a ordem escolhida foi')
print(lista)