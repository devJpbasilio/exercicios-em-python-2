# Faça uma função que receba uma lista de números e retorne a média deles.


def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros)/len(numeros)


lista_numeros = list(map(int, input("Digite numeros inteiros separado por espaço: ").split()))

print(f"A media dos numeros: {calcular_media(lista_numeros):.2f}")
