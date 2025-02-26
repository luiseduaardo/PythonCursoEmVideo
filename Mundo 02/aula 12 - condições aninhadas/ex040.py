a = float(input('primeira nota: '))
b = float(input('segunda nota: '))
media = (a+b)/2

if media < 5:
    print(f'sua média é {media}. você foi \033[7;31mREPROVADO\033[m.')
elif 5 < media < 6.9:
    print(f'sua média é {media}. você está em \033[7;33mRECUPERAÇÃO\033[m.')
else:
    print(f'sua média é {media}. parabéns, você foi \033[7;32mAPROVADO\033[m!')
