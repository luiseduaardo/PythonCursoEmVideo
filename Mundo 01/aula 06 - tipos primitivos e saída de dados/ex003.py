a = int(input('me diga um número '))
b = int(input('me diga outro número '))
soma = a + b
#print('a soma entre', a,'e',b,'vale',soma)
#print('a soma entre {} e {} vale {}'.format(a, b, soma))
print(f'a soma entre \033[33m{a} e \033[33m{b} vale \033[2;30;43m {soma} \033[m')