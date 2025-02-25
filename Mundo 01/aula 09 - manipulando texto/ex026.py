frase = str(input('escreva uma frase qualquer: ')).strip().lower()
print(f'''a letra a aparece {frase.count('a')} vezes
a primeira letra a está na posição {frase.find('a')+1}
a última letra a está na posição {frase.rfind('a')+1}''')