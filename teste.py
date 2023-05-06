""" 
luigi ferrara rm98047
davi guerra 
Rui  Amorim Siqueira98436
caua
carlos eduardo
"""

#criando lista para salvar variaveis
nome = []
cnpjj = []
quant = []
vlt = []
qntestoque=[]

#criando menu principal
while True:
    opcao = int(input("Digite a opção desejada:\n1 para controle de estoque\n2 para controle de compras\n"))
    
    
    #criando opçoes de controle de estoque 
    match opcao:
        case 1: #criando a opção controle de estoque
            opestoque = int(input("Digite\n1 para ver o estoque\n2 para registrar venda\n3 historico de compra \n"))
            if opestoque == 1:#criando opção para ver produtos no estoque
                if not any(quant): # verificando se existem itens no estoque
                    print("Não há itens no estoque.")
                else: #mostrando itens no estoque
                    for i in range(len(nome)):
                        print(f"No momento temos {quant[i]} itens do tipo {nome[i]}")
            elif opestoque == 2:# criando a opção de registro de venda
                nome_produto = input("Digite o nome do produto que foi vendido: ") # pedindo nome do produto vendido
                quantidade_retirar = int(input("Digite a quantidade que deseja retirar: "))# pedindo a quantidade de produtos vendidos
                produto_encontrado = False
                for i in range(len(nome)):#iterando todos os itens da lista
                    if nome[i] == nome_produto:# verificando se o produto esta no estoque
                        produto_encontrado = True
                        if quantidade_retirar > quant[i]:# verificando se a quantidade a retirar é maior que a quantidade de itens no estoque
                            print("Não é possível retirar essa quantidade, pois o estoque atual é menor.")
                            break
                        quant[i] -= quantidade_retirar# fazendo a subtração
                        print(f"{quantidade_retirar} itens do produto {nome_produto} foram retirados do estoque.")
                        break
                if not produto_encontrado:
                    print(f"O produto {nome_produto} não está no estoque.")
                    
            elif opestoque==3:     
                 if not any(nome):#verificando se tem numeros diferenets de zero na variavel nome
                        print("Nenhuma compra foi registrada.")
                 else:
                        print("\nHistórico de compras:")
                        for i in range(len(nome)):#usando o tamanho da variavel nome para fazer a impressão do historico
                            #imprimindo historico
                            print(f"CNPJ do fornecedor: {cnpjj[i]}")
                            print(f"Nome do produto: {nome[i]}")
                            print(f"Quantidade: {qntestoque[i]}")
                            print(f"Valor total da compra: {vlt[i]}\n")        
        #criando a opção de controle de compra        
        case 2:
            while True:
                opcao2 = int(input("Digite:\n1 para registrar compra de produto\n2 para ver histórico de compras\n3 produtos no estoque\n"))# criando submenu de controle de compra

                if opcao2 == 1:#pedindo informaçoes do produto
                    cnpj = input("Digite o CNPJ do fornecedor: ")
                    nompr = input("Digite o nome do produto comprado: ")
                    descricao = input("Digite a descrição do produto: ")
                    preco = float(input("Digite o preço do produto: "))
                    quantidade = int(input("Digite a quantidade que comprou: "))
                    valort = quantidade * preco #calculando o valor total
                           
                    #salvando o valor nas arrays que foram criadas no inicio do codigo
                    nome.append(nompr)
                    cnpjj.append(cnpj)
                    quant.append(quantidade)
                    vlt.append(valort)
                    qntestoque.append(quantidade)
                    
                    #imprimindo os valores das variaveis que foram pedidas acima
                    print("\nResumo da compra:")
                    print(f"CNPJ do fornecedor: {cnpj}")
                    print(f"Nome do produto: {nompr}")
                    print(f"Descrição: {descricao}")
                    print(f"Quantidade: {quantidade}")
                    print(f"Valor total da compra: {valort}\n")
                    
                elif opcao2 == 2:#criando a opção de registro de compras
                    if not any(nome):#verificando se ja existe algo na variavel nome 
                        print("Nenhuma compra foi registrada.")#imprimindo resposta caso n tenha nada na variavel nome
                    else:
                        print("\nHistórico de compras:")
                        for i in range(len(nome)):#usando o tamanho da variavel nome para realizar as iterações
                            #imprimindo os valores
                            print(f"CNPJ do fornecedor: {cnpjj[i]}")
                            print(f"Nome do produto: {nome[i]}")
                            print(f"Quantidade: {qntestoque[i]}")
                            print(f"Valor total da compra: {vlt[i]}\n")
                            
                elif opcao2 == 3:#criando opção de ver o estoque 
                 if not any(quant):#verificando se itens no estoque
                    print("Não há itens no estoque.") #imprimindo menssagem para tal condição
                 else:
                    for i in range(len(nome)):#usando o tamanho da variavel nome
                        print(f"No momento temos {quant[i]} itens do tipo {nome[i]}")#imprimindo estoque      
                else:
                    print("Opção inválida. Tente novamente.")
                #dando a opçao de voltar para o menu principal ou permanecer no submenu de compras
                continuar = input("\nDeseja continuar? Digite 's' para continuar ou qualquer outra tecla para voltar para o menu.\n")#pedindo valor para a vriavel continuar
                if continuar != 's': #realizando comparação do valor da variavel igual
                    break#voltando para o menu principal
                
        case _:# criando uma menssagem para caso o  usuario aperte uma tecla não configurada
            print("Opção inválida. Tente novamente.")

