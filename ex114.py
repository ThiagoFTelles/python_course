"""
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""
import urllib.request as request
import urllib.error

try:
    site = request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu erro')
else:
    print('Consegui acessar o site do pudim com sucesso!')
    print(site.read())
