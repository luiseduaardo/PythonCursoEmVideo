n = input('digite algo: ')
print('o tipo primitivo é', type(n))
print('é minúsculo? ', n.islower())
print('é decimal? ', n.isdecimal())
print('é maiúsculo? ', n.isupper())
print('é alfanumérico? ', n.isalnum())
print('é um número?', n.isnumeric())
print('está capitalizado?', n.istitle())