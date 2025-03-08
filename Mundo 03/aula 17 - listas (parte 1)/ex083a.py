# A lógica desse programa envolve adicionar 1 ao contador a cada ( e diminuir 1 do contador a cada )
# Caso apareça um ) antes do (, tornando o contador negativo, o programa encerra e torna inválido
# Caso ao fim da expressão, o número de ( e ) seja diferente, o contador é diferente de zero, tornando inválido

exp = list(str(input('Digite uma expressão: ')))

cont = 0

for c in exp:
    if c == '(':
        cont += 1
    if c == ')':
        cont -= 1
    if cont < 0:
        break

if cont != 0:
    print('Expressão inválida')
else:
    print('Expressão válida')
