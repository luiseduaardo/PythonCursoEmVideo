def voto(i):
    from datetime import datetime
    idade = datetime.now().year - i
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
