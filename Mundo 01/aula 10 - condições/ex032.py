ano = int(input('me diga um ano qualquer: '))
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')
