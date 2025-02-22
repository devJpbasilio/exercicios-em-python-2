from functools import reduce

palavras = ["Python", "é", "uma", "linguagem", "incrível"]

frase = reduce(lambda x, y: x + " " + y, palavras)
print(frase)