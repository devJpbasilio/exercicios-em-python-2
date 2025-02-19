# Elevar Números ao Quadrado
# Utilize map e uma função lambda para elevar cada número de uma lista ao quadrado.

numeros = [1, 2, 3, 4, 5]

somaQuadrados = list(map(lambda x: x ** 2, numeros))
print(somaQuadrados)