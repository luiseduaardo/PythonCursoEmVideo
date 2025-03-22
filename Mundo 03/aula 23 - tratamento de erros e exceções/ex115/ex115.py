from lib import interface, arquivo
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo.arquivoexiste(arq):
    arquivo.criararquivo(arq)

while True:
    resp = interface.menu('Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do sistema')
    if resp == 1:
        arquivo.lerarquivo(arq)
    elif resp == 2:
        interface.titulo('NOVO CADASTRO')
        nome = str(input('Nome: ')).title().strip()
        idade = interface.leiaint('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resp == 3:
        interface.titulo('Saindo do sistema... Até logo.')
        break
    else:
        print('\033[1;31mERRO. Digite uma opção válida.\033[m')
    sleep(1)
