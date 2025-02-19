from functools import reduce

numeros = [5, 10, 15]

soma = reduce(lambda x, y: x + y, numeros)

print(soma)
