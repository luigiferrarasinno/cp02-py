# Criando o catálogo com 5 produtos
catalogo = {
    "1": {"produto": "Cabernet Franc Gran Reserva ", "preco": 110.00 , "quantidade": 5},
    "2": {"produto": "Carmenere Reserva", "preco": 120.00 , "quantidade": 5},
    "3": {"produto": "Chianti Clássico ", "preco": 120.00 , "quantidade": 5},
    "4": {"produto": "Tempranillo Gran Reserva", "preco": 150.00, "quantidade": 5},
    "5": {"produto": "Tempranillo Gran Reserva", "preco": 180.00, "quantidade": 5}
}

# Imprimindo o catálogo para o cliente
print("Catálogo de produtos:")
for codigo, produto in catalogo.items():
    print(f"{codigo} - {produto['produto']} - R${produto['preco']}")

# Solicitando ao cliente qual produto deseja e a quantidade
codigo_produto = input("Digite o código do produto desejado: ")
quantidade = int(input("Digite a quantidade desejada: "))

# Obtendo o produto escolhido
produto_escolhido = catalogo[codigo_produto]

# Calculando o valor total da compra
valor_total = quantidade * produto_escolhido["preco"]

# Imprimindo as informações da compra
print(f"\nProduto escolhido: {produto_escolhido['produto']}")
print(f"Preço unitário: R${produto_escolhido['preco']}")
print(f"Quantidade: {quantidade}")
print(f"Valor total: R${valor_total}")

print("Obrigado pela compra! Volte sempre.")
