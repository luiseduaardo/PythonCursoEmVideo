teste = list()
teste.append('Gustavo')
teste.append(22)

galera = list()
galera.append(teste[:])      # [:] faz a cópia
teste[0] = 'Maria'
teste[1] = 40
galera.append(teste)

print(galera)
