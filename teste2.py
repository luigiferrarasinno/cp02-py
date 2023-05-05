nome = []
cnpjj = []
quant = []
vlt = []

while True:
    opcao = int(input("Digite a opção desejada:\n1 para controle de estoque\n2 para controle de compras\n"))
    
    match opcao:
        case 1:
            opestoque = int(input("Digite\n1 para ver o estoque\n2 para retirar item do estoque\n"))
            if opestoque == 1:
                if not any(quant):
                    print("Não há itens no estoque.")
                else:
                    for i in range(len(nome)):
                        print(f"No momento temos {quant[i]} itens do tipo {nome[i]}")
            elif opestoque == 2:
                nome_produto = input("Digite o nome do produto que deseja retirar: ")
                quantidade_retirar = int(input("Digite a quantidade que deseja retirar: "))
                produto_encontrado = False
                for i in range(len(nome)):
                    if nome[i] == nome_produto:
                        produto_encontrado = True
                        if quantidade_retirar > quant[i]:
                            print("Não é possível retirar essa quantidade, pois o estoque atual é menor.")
                            break
                        quant[i] -= quantidade_retirar
                        print(f"{quantidade_retirar} itens do produto {nome_produto} foram retirados do estoque.")
                        break
                if not produto_encontrado:
                    print(f"O produto {nome_produto} não está no estoque.")
                
        case 2:
            while True:
                opcao2 = int(input("Digite:\n1 para registrar compra de produto\n2 para ver histórico de compras\n"))

                if opcao2 == 1:
                    cnpj = input("Digite o CNPJ do fornecedor: ")
                    nompr = input("Digite o nome do produto comprado: ")
                    descricao = input("Digite a descrição do produto: ")
                    preco = float(input("Digite o preço do produto: "))
                    quantidade = int(input("Digite a quantidade que comprou: "))
                    valort = quantidade * preco

                    nome.append(nompr)
                    cnpjj.append(cnpj)
                    quant.append(quantidade)
                    vlt.append(valort)

                    print("\nResumo da compra:")
                    print(f"CNPJ do fornecedor: {cnpj}")
                    print(f"Nome do produto: {nompr}")
                    print(f"Descrição: {descricao}")
                    print(f"Quantidade: {quantidade}")
                    print(f"Valor total da compra: {valort}\n")
                elif opcao2 == 2:
                    if not any(nome):
                        print("Nenhuma compra foi registrada.")
                    else:
                        print("\nHistórico de compras:")
                        for i in range(len(nome)):
                            print(f"CNPJ do fornecedor: {cnpjj[i]}")
                            print(f"Nome do produto: {nome[i]}")
                            print(f"Quantidade: {quant[i]}")
                            print(f"Valor total da compra: {vlt[i]}\n")
                else:
                    print("Opção inválida. Tente novamente.")

                continuar = input("\nDeseja continuar? Digite 's' para continuar ou qualquer outra tecla para voltar para o menu.\n")
                if continuar != 's':
                    break
        case _:
            print("Opção inválida. Tente novamente.")
