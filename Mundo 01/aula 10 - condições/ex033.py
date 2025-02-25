a = int(input('escolha um número qualquer: '))
b = int(input('escolha outro número qualquer: '))
c = int(input('por fim, escolha outro número: '))
# Verificando quem é o menor
if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c
# Verificando quem é o maior
if a>b and a>c:
    maior = a
if b>c and b>a:
    maior = b
if c>b and c>a:
    maior = c
print(f'o maior número é {maior} e o menor número é {menor}')
