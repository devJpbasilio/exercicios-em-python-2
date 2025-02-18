# Crie uma função que receba dois números e retorne o maior deles.

def maior(a, b):
    if a > b:
        return a
    else:
        return b


num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

print(f"O maior é: {maior(num1, num2)}")
