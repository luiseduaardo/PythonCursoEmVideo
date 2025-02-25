sal = float(input('qual o seu salário? R$'))
if sal <= 1250:
#    print(f'o seu novo salário é de R${sal*1.15:.2f}')
    novo = 1.15*sal
else:
#    print(f'o seu novo salário é de R${sal*1.10:.2f}')
    novo = 1.10*sal
print(f'o seu novo salário é de R${novo:.2f}')