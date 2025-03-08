# A lógica desse programa consiste em adicionar um ( a cada aparição e remover a cada )
# Caso apareça um ) sem um ( na lista, o programa adiciona um ) na lista e encerra, tornando a expressão inválida

exp = str(input('Digite sua expressão: '))
pilha = []

for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')
