# Importando módulos inteiros = import moduloName
# Ex: import math

# Importando apenas uma ou algumas partes do módulo math
# Ex: from math import ceil, sqrt, trunc

# ceil = arredondar pra cima
# floor = arredondar para baixo
# trunc = eliminar da vírgula pra frente
# sqrt = raiz quadrada
# factorial = fatorial

# Depois de digitar "from math import" eu aperto ctrl+espaço e ele me mostra todas as funções disponíveis
# Se eu importar math inteira, eu chamo a função assim: math.sqrt(num)
# Se eu importar apenas a função, eu chamo ela direto: sqrt(num)
import random
from math import sqrt

num = random.randint(1, 10)
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

# Importando bibliotecas externas: Primeiro eu coloco o comando "import emoji" e depois ele me dá as opções para eu
# clicar em qual library eu quero instalar.
# para ver as bibliotecas externas instaladas eu vou em File/Settings/Project xxx/Interpreter
import emoji
print(emoji.emojize('Olá mundo :sunglasses:!', use_aliases=True))
