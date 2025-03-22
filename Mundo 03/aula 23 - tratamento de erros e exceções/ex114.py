import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except OSError:
    print('\n\033[1;31mO site Pudim não está disponível no momento\033[m')
else:
    print('\n\033[1;32mConsegui acessar o site Pudim com sucesso\033[m')