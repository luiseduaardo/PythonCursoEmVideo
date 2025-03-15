from datetime import datetime

fun = dict()

fun['nome'] = str(input('Nome: ')).strip().title()
fun['ano'] = int(input('Ano de nascimento: '))
fun['idade'] = datetime.now().year - fun['ano']
fun['sexo'] = str(input('Sexo: ')).strip()
fun['ctps'] = int(input('Carteira de Trabalho (caso não tenha, digite 0): '))

if fun['ctps'] != 0:
    fun['salário'] = float(input('Salário: R$'))
    fun['contratação'] = int(input('Ano da contratação: '))
    if fun['sexo'][0] in 'Mm':
        fun['aposentadoria'] = fun['contratação'] + 35 - fun['ano']
    if fun['sexo'][0] in 'Ff':
        fun['aposentadoria'] = fun['contratação'] + 30 - fun['ano']

print('-=' * 30)

for k, v in fun.items():
    print(f'{k} é igual a {v}')
