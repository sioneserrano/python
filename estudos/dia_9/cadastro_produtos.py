produtos = []


def cadastrar_produto(produtos):

    print("\nCadastro produto")
    
    nome = input("Nome: ")
    preco = tratar_erro("Preço: ")
    
    produtos.append({"nome": nome, "preco": preco})
    print("Produto cadastrado!\n")
   

def listar_produtos(produtos):

    print("\nLista de produtos")
    cadastro_vazio(produtos)
    i = 0
    while i < len(produtos):
        print(f"{i+1} - Nome: {produtos[i]['nome']}|Preço: {produtos[i]['preco']}")
        i += 1
    print("\n")

    
def mostrar_produto_mais_caro(produtos):

    cadastro_vazio(produtos)
    if len(produtos) != 0:
        i = 0
        indice_maior = 0
        maior = produtos[0]["preco"]
        while i < len(produtos):
            if produtos[i]["preco"] > maior:
                maior = produtos[i]["preco"]
                indice_maior = i
            i+=1
    
        print("\nProduto mais caro")
        print(f"Nome: {produtos[indice_maior]["nome"]}|Preço: {produtos[indice_maior]["preco"]}")


def mostrar_preco_media(produtos):

    cadastro_vazio(produtos)
    if len(produtos) != 0:
        i = 0
        soma = 0
        while i < len(produtos):
            soma += produtos[i]["preco"] 
            i+=1
        media = soma / len(produtos)
        print("\nPreço médio dos produtos")
        print(f"Media: {media:.2f}")


def buscar_produto(produtos):
    cadastro_vazio(produtos)

    if len(produtos) != 0:
        
        print("\nBusca de produto")
        produto = input("Digite o produto: ")

        i = 0
        encontrado = {}
        while i < len(produtos):
            if produtos[i]["nome"] == produto:
                encontrado = {"Nome": produtos[i]["nome"], "Preco": produtos[i]["preco"]}
            i+=1
        
        if encontrado == {}:
            print("Produto não encontrado.")

        else:
            print(f"\nProduto encontrado:")
            for key, value in encontrado.items():
                print(f"{key}: {value}")

def tratar_erro(texto):

    while True:
        try:
            numero = float(input(texto))
            if numero >= 0:
                return numero
            else:
                print("Informe um valor positivo!")
        except ValueError:
            print("Informe um numero!")

def menu():

    print("\n1 - Cadastrar produto \n2 - Listar produtos \n3 - Mostrar produto mais caro \n4 - Mostrar preço médio \n5 - Buscar produto \n6 - Sair")

def cadastro_vazio(produtos):
    if len(produtos) == 0:
        print("\nNenhum produto encontrado!\n")

while True:

    menu()
    opcao = tratar_erro("Digite uma opção: ")

    if opcao == 1:
        cadastrar_produto(produtos)
    elif opcao == 2:
        listar_produtos(produtos)
    elif opcao == 3:
        mostrar_produto_mais_caro(produtos)
    elif opcao == 4:
        mostrar_preco_media(produtos)
    elif opcao == 5:
        buscar_produto(produtos)
    elif opcao == 6:
        print("Saindo...\n")
        break
    else:
        print("\nOpção inválida!\n")