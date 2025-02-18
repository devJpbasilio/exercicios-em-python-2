# Escreva uma função que receba um nome e retorne uma saudação personalizada.

def saudacao(nome):
    return f"Olá, {nome}! Seja bem-vindo(a) ao Python!"

nome = input('Digite seu nome: ')
print(saudacao(nome))