# Crie um programa que peça 5 números ao usuário e os armazene em uma lista.
# Em seguida, exiba o maior e o menor número da lista.

# numeros = list(map(int, input("Digite 5 numeros separados por espaço: ").split()))
#
# print(f"O maior número é: {max(numeros)}, o menor número é: {min(numeros)}")

numeros = []

for i in range(5):
    while True:
        try:
            num = float(input(f"Digite o {i+1}º número: "))
            numeros.append(num)
            break
        except ValueError:
            print("Entrada inválida. Tente novamente!")

print(f"O maior número é: {max(numeros):.2f}, o menor número é: {min(numeros):.2f}")