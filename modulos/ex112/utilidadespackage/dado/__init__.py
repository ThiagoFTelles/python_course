def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31m"{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[;31mERRO! Digite um número inteiro válido.\033[m')
            continue # O continue joga de volta pro laço novamente (recomeça o while)
        except KeyboardInterrupt:
            print('\033[;31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[;31mERRO! Digite um número real válido.\033[m')
            continue # O continue joga de volta pro laço novamente (recomeça o while)
        except KeyboardInterrupt:
            print('\033[;31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n
