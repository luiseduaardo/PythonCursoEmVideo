from .. import interface

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')     # Leitura de arquivo texto (read text)
        a.close()
        return True
    except FileNotFoundError:
        return False


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')    # Criação de arquivo texto (write text +)
        a.close()
        print(f'Arquivo {nome} criado com sucesso')
    except:
        print('Houve um erro na criação do arquivo.')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
        interface.titulo('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    except:
        print('Erro ao ler o arquivo')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
            print(f'Novo registro de {nome} adicionado.')
            a.close()
        except:
            print('Houve um erro na escrita dos dados.')
