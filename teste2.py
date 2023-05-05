opcao = int(input("Digite a opção desejada: \n 1 para controle de estoque \n 2 para realizar novas compras \n "))

match opcao:
    case 2:
     print("opção de realizar nova compra selecionada")
     cnpj= input("digite o cnpj para continuar: ")
     catalogo = [ 

    {"codigo": 1, "produto": "Cabernet Franc Gran Reserva ", "preco": 110.00, }, 

    {"codigo": 2, "produto": "Carmenere Reserva", "preco": 120.00 ,}, 

    {"codigo": 3, "produto": "Chianti Clássico ", "preco": 120.00 , }, 

    {"codigo": 4, "produto": "Tempranillo Gran Reserva", "preco": 150.00, }, 

    {"codigo": 5, "produto": "Chardonnay", "preco": 180.00, } 

] 

 
 

# Imprimindo o catálogo 

print("Catálogo de produtos:") 

for produto in catalogo: 

      print(f"{produto['codigo']} - {produto['produto']} - R${produto['preco']}") 

 
 

# Solicitando ao cliente quais produtos deseja e as quantidades 

carrinho = [] 

continuar_comprando = True 

while continuar_comprando: 

    codigo_produto = int(input("Digite o código do produto desejado (ou 0 para finalizar): ")) 

    if codigo_produto == 0: 

        continuar_comprando = False 

    else: 

        quantidade = int(input("Digite a quantidade desejada: ")) 

        produto_escolhido = next((produto for produto in catalogo if produto['codigo'] == codigo_produto), None) 

        if produto_escolhido: 

            carrinho.append({"produto": produto_escolhido['produto'], "preco": produto_escolhido['preco'], "quantidade": quantidade}) 

 
 

# Calculando o valor total da compra 

valor_total = sum(produto['preco'] * produto['quantidade'] for produto in carrinho) 

 
 

# Imprimindo as informações da compra 

print("\nProdutos escolhidos:") 
print(f"\ncnpj:{cnpj}")

for produto in carrinho: 

 print(f"{produto['quantidade']} x {produto['produto']} - R${produto['preco']}") 

print(f"\nValor total da compra: R${valor_total}") 


 

