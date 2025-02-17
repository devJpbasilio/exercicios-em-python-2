#  Loops (for, while)
# Faça um programa que peça um número e exiba a tabuada dele (de 1 a 10).

print("----Programa Tabuada----")
n = int(input("Digite um número que deseja ver a Tabuada: "))

for c in range(1, 11):
    print(f"{n} x {c} = {n * c}")