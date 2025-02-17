# Loops (for, while)
# Peça um número ao usuário e some todos os números de 1 até esse número.

numero = int(input("Digite um número: "))

soma = 0

for i in range(1, numero + 1):
    soma += i

print(f"A soma de 1 até {numero} é {soma}")