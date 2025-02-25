s = float(input('qual o seu salário hoje? R$'))
a = float(input('qual o aumento prometido em %? '))
print(f'o seu novo salário será de R${(1+(a/100))*s:.2f}')