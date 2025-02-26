nome = str(input('Qual o seu nome? '))
print(f'Seja bem vindo, Sr(a) {nome}!')
val = float(input('Qual o valor do imóvel que você deseja adquirir? R$'))
ano = int(input('Em quantos anos você pretende pagar esse imóvel? '))
sal = float(input('Qual o seu salário mensal? R$'))
parcela = val/(ano*12)

if parcela > (sal*0.3):
    print(f'Sr(a), a sua parcela estimada deveria ficar no valor de \033[4;34mR${parcela:.2f}\033[m, o que equivale a \033[1;31m{parcela*100/sal:.2f}%\033[m do seu salário')
    print(f'Por esse motivo, infelizmente o seu empréstimo foi \033[1;7;31mNEGADO\033[m')
else:
    print(f'Parabéns Sr(a) {nome}! O seu empréstimo foi \033[1;7;32mAPROVADO\033[m')
    print(f'A sua parcela será no valor de \033[4;34mR${parcela:.2f}\033[m, o que equivale a \033[1;32m{parcela*100/sal:.2f}%\033[m do seu salário.')
