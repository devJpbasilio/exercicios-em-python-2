# Crie um programa que receba uma frase e conte quantas vezes cada palavra aparece.

from collections import Counter

frase = input("Digite uma frase: ").lower()

palavras = frase.split()
contagem = Counter(palavras)

for palavra, quantidade in contagem.items():
    print(f"{palavra}: {quantidade} vezes")
