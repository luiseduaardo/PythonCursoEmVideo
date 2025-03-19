def contador(*num):
    soma = 0
    for v in num:
        soma += v
    print(f'a soma dos {len(num)} valores em {num} é {soma}')

contador(1,4,6,4,2,8)
contador(4,5,6,3,1,4,9,10,4)
contador(1,2)
