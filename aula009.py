# Manipulando Strings

# frase com 21 caracteres (da posição 0 à 20)
string = 'Curso em Vídeo Python'


# ---------- Fatiamento ----------
print(string[9])
# Pega o caractere 9 = 'V'

print(string[9:14])
# pega da posição 9 até a 13 = 'Vídeo'

print(string[9:21])
# pega da posição 9 até a 20 = 'Vídeo python'

print(string[9:21:2])
# pega da posição 9 até a 20, pulando de 2 em 2 = 'VdoPto'

print(string[:5])
# pega do início da string até o caractere 4 = 'Curso'

print(string[15:])
# pega do caractere 15 até o final = 'Python'

print(string[9::])
# pega do caractere 9 até o final, pulando de 3 em 3 = 'VePh'

# ---------- Length ----------
print(len(string))
# length = 21

# ---------- Count ----------
string.count('o')
# conta quantos o minúsculo tem na string = 3

string.count('o', 0, 13)
# conta quantos 'o' tem do caractere 0 ao 12 = 1

# ---------- Find ----------
string.find('deo')
# retorna a posição inicial onde apareceu 'deo' = 11

string.find('Android')
# retorna valor -1 o que significa que não foi encontrado

print('Curso' in string)
# operador que retorna True

# ---------- Métodos de manipulação ----------

print(string.replace('Python', 'Android'))
print(string.upper())
print(string.lower())

print(string.capitalize())
# Apenas a primeira letra da frase em maiúsculo

print(string.title())
# Primeira letra de cada palavra em maiúsculo

print(string.strip())
# Remove os espaços excedentes no início e no final da string

print(string.lstrip())
# Remove os espaços excedentes apenas no início (left) da string

print(string.rstrip())
# Remove os espaços excedentes apenas no final (right) da string

# ---------- Divisão ----------

lista_split = string.split()
# Cria uma lista de string com cada palavra = ['Curso', 'em', 'Vídeo', 'Python']

print('-'.join(lista_split))
# junta as strings da lista, separadas por '-' = 'Curso-em-Vídeo-Python'

# print de textos grandes com quebra de linha usando 3 aspas """xxx""":
print("""Lorem Ipsum is simply dummy text of the printing 
and typesetting industry. Lorem Ipsum has been the industry's 
standard dummy text ever since the 1500s, when an unknown printer took 
a galley of type and scrambled it to make a type specimen book.""")
