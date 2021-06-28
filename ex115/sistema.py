from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver cadastros', 'Novo cadastro', 'Sair do sistema'])
    if resposta == 1:
        # Ver cadastros:
        ler_arquivo(arq)
    elif resposta == 2:
        # Novo cadastro:
        cabecalho('NOVO CADASTRO')
        nome = str(input('NOME: '))
        idade = leiaint('IDADE: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Sair:
        cabecalho('Saindo do sistema...')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
        sleep(1.5)
