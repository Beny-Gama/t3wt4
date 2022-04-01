# IMPORTAR BIBLIOTECAS EM PYTHON

# generalista = import "biblioteca"
# especialista = from "biblioteca" inport

# Ex:
# math
# ceil     = arredonda para cima
# floor    = arredenda para baixo
# trunc    = trunca a numero (eleima o que vem antes da virgula de um numero)
# paw      = potencia = **
# sqrt     = rais quadrada
# fatorial = fatorial

# generalista  = inport "math"
# especialista = from "math" inport "sqrt"
from math import sqrt
num = int(input('dgite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é iqual a {:.2f}'
      .format(num, raiz))

import random
num2 = random.random()
print(num2)


