try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except ZeroDivisionError:
    # Eu posso ter um except para cada tipo de exceção
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt: # Este aqui acontece quando o programa é interrompido
    print('O usuário não informou os dados')
except (ValueError, TypeError):
    print('Digite um valor válido')
except Exception as erro:
    # este aqui é um except "mais geral"
    print(f'Infelizmente tivemos o seguinte problema : {erro.__class__}')
else: # Opcional
    # Dentro do else eu digo o que acontece se meu "try" der certo.
    print(f'O resultado é {r:.1f}')
finally: # Opcional
    # O que estiver no finally acontece independente se o try der certo ou não.
    print('FIM')
