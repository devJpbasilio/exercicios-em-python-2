

# numero = int(input('Digite um número: '))
# verificar = (lambda x: 'Está no intervalo!' if x in range(1, 11)
#                 else 'Não está no intervalo!')
# print(verificar(numero))

numero = int(input('Digite um número: '))
multiplicacao = lambda x: [x * i for i in range(1, 11)]
print(multiplicacao(numero))