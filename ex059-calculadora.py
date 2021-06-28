"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
opcao = 0

while opcao!= 5:
    print("""    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa""")
    opcao = int(input('>>>>>> Qual a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma é {}'.format(soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O produto é {}'.format(produto))
    elif opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print('Entre {} e {}, o maior é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('informe os números novamente:')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente:')
    print('-='*10)
print('Fim do programa! Volte Sempre!')
