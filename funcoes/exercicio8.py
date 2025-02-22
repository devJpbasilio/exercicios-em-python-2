# Exercício com map()
# Dada a lista de preços abaixo, escreva um código que
# aplique um desconto de 10% em cada item.
#
# precos = [100, 250, 50, 400, 150]
#
# Saída esperada (aproximada):
#
# [90.0, 225.0, 45.0, 360.0, 135.0]

precos = [100, 250, 50, 400, 150]

novo_preco = list(map(lambda x: x * (1 - 10 / 100), precos))

print(novo_preco)