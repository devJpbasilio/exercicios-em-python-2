# Exercício com filter()
# Dada a lista de idades abaixo, filtre apenas as idades maiores ou iguais a 18 anos.
# idades = [12, 17, 19, 24, 15, 30, 8]

# Saída esperada:
# [19, 24, 30]


idades = [12, 17, 19, 24, 15, 30, 8]

maior_idade = list(filter(lambda idade: idade >= 18, idades))

print(maior_idade)