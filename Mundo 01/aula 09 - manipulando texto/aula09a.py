frase = 'Curso em Vídeo Python'
frase2 = ['Curso', 'em', 'Vídeo', 'Python']

#fatiamento
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[5:])
print(frase[9::3])

#análise
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

#transformação
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.lstrip())
print(frase.rstrip())

#divisão e junção
print(frase.split())
print(' '.join(frase2))