print('----- CADASTRADOR DE DADOS -----')

maior = homem = mul20 = cont = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '

    while sexo not in 'FfMm':
        sexo = str(input('Sexo: ')).strip()[0]

    cont += 1

    if idade >= 18:
        maior += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mul20 += 1

    print('-' * 32)
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? ')).strip()[0]
    print('-' * 32)

    if continuar in 'Nn':
        break

print('contagem ENCERRADA')
print(f'das {cont} pessoas cadastradas, foram obtidos os seguintes resultados:')
print(f'''{maior} pessoas maiores de idade;
{homem} homens;
{mul20} mulheres com menos de 20 anos.''')
