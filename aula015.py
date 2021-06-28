# Curso Python #15 - Interrompendo repetições while
n = s = 0
while True: # loop infinito
    n = int(input('Digite um número: '))
    if n == 999:
        break # interrompe o loop
    s += n
print(f'A soma vale {s}')

# fString:
nome = 'josé'
salario = 985.3

print(f'o {nome:-^20} ganha {salario:.2f}')