# Condicionais (if, elif, else)
# Peça três números e exiba o maior deles.

print("-----Qual o maior número?-----")
numeros = list(map(int, input("Digite 3 números separado de espaço: ").split()))

maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero


print(f"O maior número é {maior}")