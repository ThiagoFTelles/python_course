# Condições Aninhadas

nome = str(input('Qual é seu nome? '))
if nome == 'Thiago':
    print('Que belo nome!')
elif nome == 'Rovena' or nome == 'Maria' or nome == 'José':
    print('Seu nome é bem comum no Brasil')
else:
    print('Seu nome é tão normal!')
print('Bom dia {}!'.format(nome))
