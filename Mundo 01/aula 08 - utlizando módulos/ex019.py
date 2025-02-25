#from random import choice
#a1 = input('me dê o nome do primeiro aluno ')
#a2 = input('me dê o nome do segundo aluno ')
#a3 = input('me dê o nome do terceiro aluno ')
#a4 = input('me dê o nome do quarto aluno ')
#print(f'o aluno escolhido foi {choice([f'{a1}', f'{a2}', f'{a3}', f'{a4}'])}')

from random import choice
a1 = input('me dê o nome do primeiro aluno ')
a2 = input('me dê o nome do segundo aluno ')
a3 = input('me dê o nome do terceiro aluno ')
a4 = input('me dê o nome do quarto aluno ')
lista = [a1,a2,a3,a4]
escolhido = choice(lista)
print(f'o aluno escolhido foi {escolhido}')