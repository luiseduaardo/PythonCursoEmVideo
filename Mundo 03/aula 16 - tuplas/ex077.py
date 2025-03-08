palavras = ('nebuloso', 'orquestra', 'fragmento', 'cobalto', 'inercia',
            'abismo', 'refugio', 'elixir', 'tangivel', 'labirinto')

for c in palavras:
    print(f'\nNa palavra {c.upper()} temos ', end = '')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
