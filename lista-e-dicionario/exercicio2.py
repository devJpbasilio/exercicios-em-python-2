# Crie um dicionário representando um produto (nome, preço e quantidade).
# Depois, peça ao usuário para atualizar a quantidade e exiba o novo dicionário.


produto = {
    "Nome": "Teclado Mecânico",
    "Preço": 250.00,
    "Quantidade": 10
}

print(f"Produto atual: {produto}")

nova_quantidade =  int(input("Digite a nova quantidade do produto: "))

produto["Quantidade"] = nova_quantidade

print(f"Produto atualizado: {produto}")