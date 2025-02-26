frase = str(input('digite sua frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('essa frase É UM PALÍNDROMO')
else:
    print('essa frase NÃO É UM PALÍNDROMO')
