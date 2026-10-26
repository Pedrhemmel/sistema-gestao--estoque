# PROJETO 1 - SISTEMA DE GESTAO DE ESTOQUE
 
produtos = {}
movimentacoes = []
 
 
def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")
 
    codigo = input("Codigo do produto: ")
 
    if codigo in produtos:
        print("Erro: esse codigo ja existe!")
        return
 
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
 
    preco = float(input("Preco do produto: R$ "))
    quantidade = int(input("Quantidade inicial: "))
 
    if preco < 0 or quantidade < 0:
        print("Preco e quantidade nao podem ser negativos.")
        return
 
    produtos[codigo] = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }
 
    print("Produto cadastrado com sucesso!")
 
 
def consultar_produto():
    print("\n--- CONSULTAR PRODUTO ---")
 
    codigo = input("Digite o codigo: ")
 
    if codigo in produtos:
        produto = produtos[codigo]
 
        print("Nome:", produto["nome"])
        print("Categoria:", produto["categoria"])
        print("Preco: R$", produto["preco"])
        print("Quantidade:", produto["quantidade"])
    else:
        print("Produto nao encontrado.")
 
 
def atualizar_produto():
    print("\n--- ATUALIZAR PRODUTO ---")
 
    codigo = input("Digite o codigo: ")
 
    if codigo in produtos:
        produto = produtos[codigo]
 
        print("1 - Atualizar nome")
        print("2 - Atualizar categoria")
        print("3 - Atualizar preco")
 
        opcao = input("Escolha uma opcao: ")
 
        if opcao == "1":
            produto["nome"] = input("Novo nome: ")
            print("Nome atualizado!")
 
        elif opcao == "2":
            produto["categoria"] = input("Nova categoria: ")
            print("Categoria atualizada!")
 
        elif opcao == "3":
            preco = float(input("Novo preco: R$ "))
 
            if preco >= 0:
                produto["preco"] = preco
                print("Preco atualizado!")
            else:
                print("Preco invalido.")
 
        else:
            print("Opcao invalida.")
 
    else:
        print("Produto nao encontrado.")
 
 
def remover_produto():
    print("\n--- REMOVER PRODUTO ---")
 
    codigo = input("Digite o codigo: ")
 
    if codigo in produtos:
        del produtos[codigo]
        print("Produto removido!")
    else:
        print("Produto nao encontrado.")
 
 
def entrada_estoque():
    print("\n--- ENTRADA DE ESTOQUE ---")
 
    codigo = input("Codigo do produto: ")
 
    if codigo in produtos:
        quantidade = int(input("Quantidade recebida: "))
 
        if quantidade > 0:
            produtos[codigo]["quantidade"] += quantidade
 
            movimentacoes.append(
                ["Entrada", codigo, quantidade]
            )
 
            print("Entrada registrada!")
        else:
            print("Quantidade invalida.")
 
    else:
        print("Produto nao encontrado.")
 
 
def saida_estoque():
    print("\n--- SAIDA DE ESTOQUE ---")
 
    codigo = input("Codigo do produto: ")
 
    if codigo in produtos:
        quantidade = int(input("Quantidade retirada: "))
 
        if quantidade <= 0:
            print("Quantidade invalida.")
 
        elif quantidade > produtos[codigo]["quantidade"]:
            print("Estoque insuficiente!")
 
        else:
            produtos[codigo]["quantidade"] -= quantidade
 
            movimentacoes.append(
                ["Saida", codigo, quantidade]
            )
 
            print("Saida registrada!")
 
    else:
        print("Produto nao encontrado.")
 
 
def listar_categoria():
    print("\n--- CONSULTAR POR CATEGORIA ---")
 
    categoria = input("Digite a categoria: ")
    encontrou = False
 
    for codigo in produtos:
        produto = produtos[codigo]
 
        if produto["categoria"].lower() == categoria.lower():
            print(
                codigo,
                "-", produto["nome"],
                "| Quantidade:", produto["quantidade"],
                "| Preco: R$", produto["preco"]
            )
            encontrou = True
 
    if not encontrou:
        print("Nenhum produto encontrado nessa categoria.")
 
 
def relatorio_geral():
    print("\n--- RELATORIO GERAL ---")
 
    total_unidades = 0
    valor_estoque = 0
 
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return
 
    for codigo in produtos:
        produto = produtos[codigo]
 
        print(
            "Codigo:", codigo,
            "| Nome:", produto["nome"],
            "| Categoria:", produto["categoria"],
            "| Quantidade:", produto["quantidade"],
            "| Preco: R$", produto["preco"]
        )
 
        total_unidades += produto["quantidade"]
        valor_estoque += (
            produto["quantidade"] * produto["preco"]
        )
 
    print("\nTotal de unidades:", total_unidades)
    print("Valor total do estoque: R$", round(valor_estoque, 2))
 
 
def historico_movimentacoes():
    print("\n--- HISTORICO DE MOVIMENTACOES ---")
 
    if len(movimentacoes) == 0:
        print("Nenhuma movimentacao registrada.")
        return
 
    for movimento in movimentacoes:
        tipo = movimento[0]
        codigo = movimento[1]
        quantidade = movimento[2]
 
        if codigo in produtos:
            nome = produtos[codigo]["nome"]
        else:
            nome = "Produto removido"
 
        print(
            tipo, "| Codigo:", codigo,
            "| Produto:", nome,
            "| Quantidade:", quantidade
        )
 
 
# MENU PRINCIPAL
 
while True:
    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Cadastrar produto")
    print("2 - Consultar produto")
    print("3 - Atualizar produto")
    print("4 - Remover produto")
    print("5 - Registrar entrada")
    print("6 - Registrar saida")
    print("7 - Consultar por categoria")
    print("8 - Relatorio geral")
    print("9 - Historico de movimentacoes")
    print("0 - Encerrar sistema")
 
    opcao = input("Escolha uma opcao: ")
 
    if opcao == "1":
        cadastrar_produto()
 
    elif opcao == "2":
        consultar_produto()
 
    elif opcao == "3":
        atualizar_produto()
 
    elif opcao == "4":
        remover_produto()
 
    elif opcao == "5":
        entrada_estoque()
 
    elif opcao == "6":
        saida_estoque()
 
    elif opcao == "7":
        listar_categoria()
 
    elif opcao == "8":
        relatorio_geral()
 
    elif opcao == "9":
        historico_movimentacoes()
 
    elif opcao == "0":
        print("Sistema encerrado!")
        break
 
    else:
        print("Opcao invalida. Tente novamente.")