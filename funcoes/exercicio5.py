# Filtrar Números Pares
# Use filter e lambda para filtrar apenas os números pares de uma lista.

import random

numeros = list(random.randint(1, 100) for _ in range(20)) # Criando lista de números aleatórios
print(numeros)

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros)) # Filtrando e usando função lambda

# Saída
print("\nFiltrando os numeros pares.")
print(numeros_pares)