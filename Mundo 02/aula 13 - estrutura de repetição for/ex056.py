mulheresMenos = 0
idadeTot = 0
homemVelho = 0
nomeVelho = 0

for n in range (1, 5):
    print(f'----- {n}ª pessoa -----')
    nome = str(input(f'Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    idadeTot += idade

    if sexo == 'F' and idade < 20:
        mulheresMenos += 1

    if sexo == 'M' and idade > homemVelho:
        homemVelho = idade
        nomeVelho = nome

print(f'a média de idade do grupo é de {idadeTot/4} anos')
print(f'o nome do homem mais velho é {nomeVelho} e ele tem {homemVelho} anos')
print(f'existem {mulheresMenos} mulheres abaixo de 20 anos')
