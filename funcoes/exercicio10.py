from functools import reduce

numeros = [3, 5, 2, 4]

calculo = reduce(lambda x, y: x * y, numeros)
print(calculo)