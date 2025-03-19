from time import sleep

c = {'vazio': '\033[m',
     'vermelho': '\033[0;30;41m',
     'branco': '\033[7;37m',
     'verde': '\033[0;30;44m'
     }

def ajd(msg):
    titulo(f'Acessando o manual do comando \'{msg}\'', 'branco')
    print(c['verde'], end = '')
    help(msg)
    print(c['vazio'], end = '')
    sleep(2)

def titulo(msg, cor = 'vermelho'):
    print(c[cor], end = '')
    print('-'*2*len(msg))
    print(f'{msg:^{2*len(msg)}}')
    print('-'*2*len(msg))
    print(c['vazio'])
    sleep(1)

titulo('SISTEMA DE AJUDA PyHELP')
comando = ''
while True:
    comando = str(input('Função ou Biblioteca >>> ')).strip()
    if comando.upper() == 'FIM':
        break
    ajd(comando)
