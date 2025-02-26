peso = float(input('qual o seu peso em kg? '))
altura = float(input('qual sua altura em m? '))
imc = peso / (altura**2)

if imc < 18.5:
    print(f'seu IMC é de {imc:.1f} e você está \033[1;7;31m ABAIXO DO PESO \033[m')
elif 18.5 <= imc < 25:
    print(f'seu IMC é de {imc:.1f} e você está no \033[1;7;32m PESO IDEAL \033[m')
elif 25 <= imc < 30:
    print(f'seu IMC é de {imc:.1f} e você está no \033[1;7;33m SOBREPESO \033[m')
elif 30 <= imc < 40:
    print(f'seu IMC é de {imc:.1f} e você está na \033[1;7;31m OBESIDADE \033[m')
else:
    print(f'seu IMC é de {imc:.1f} e você está na \033[1;7;31m OBESIDADE MÓRBIDA \033[m')
