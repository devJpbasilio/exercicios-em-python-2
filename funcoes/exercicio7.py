

frase = "List comprehension é poderoso"

frase_invertida = ' '.join([palavra[::-1] for palavra in frase.split()])

print(frase)
print(frase_invertida)