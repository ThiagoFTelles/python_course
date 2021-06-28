primeiro_numero = int(input('Digite um número: '))
segundo_numero = int(input('Digite outro número: '))
soma = primeiro_numero + segundo_numero
teste = input('digite qualquer coisa: ')
print('Resultado da soma entre {} e {} é igual a {}'.format(primeiro_numero, segundo_numero, soma))
# posso definir a ordem dos formats se eu quiser
# ex: 'Resultado da soma entre {0} e {1} é igual a {2}'
print(type(teste))
print('o teste é numérico? R: {}'.format(teste.isnumeric()))
