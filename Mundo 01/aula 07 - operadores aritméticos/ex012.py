p = float(input('qual o preço do objeto que você quer comprar? R$'))
d = float(input('qual o desconto em % que será dado? '))
print(f'o preço do objeto com o desconto é de R${(1-(d/100))*p:.2f}')