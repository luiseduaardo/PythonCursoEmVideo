from datetime import date
ano = int(input('em que ano você nasceu? '))
idade = date.today().year-ano

if idade <= 9:
    print('você é um atleta MIRIM')
elif 9 < idade <= 14:
    print('você é um atleta INFANTIL')
elif 14 < idade <= 19:
    print('você é um atleta JÚNIOR')
elif 19 < idade <= 25:
    print('você é um atleta SÊNIOR')
else:
    print('você é um atleta MASTER')
