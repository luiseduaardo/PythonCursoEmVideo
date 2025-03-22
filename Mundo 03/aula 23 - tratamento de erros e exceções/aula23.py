try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    d = a / b

# Mostra diferentes mensagens para diferentes tipos de erro
except (ValueError, TypeError):
    print('Tivemos problemas com o tipo de valor')

except ZeroDivisionError:
    print('Não é possível dividir por zero')

# Fala o tipo de erro
except Exception as erro:
    print(f'O erro foi o seguinte: {erro.__class__}')

else:
    print(d)

finally:
    print('-- Programa encerrado -- ')
