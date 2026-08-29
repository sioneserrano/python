produtos = []


def cadastrar_produto(produtos):

    print("\nCadastro produto")
    

    nome = input("Nome: ")
    preco = tratar_erro("Preço: ")
    
    produtos.append({"nome": nome, "preco": preco})
    print("Produto cadastrado!\n")
   


def listar_produtos():
    print()
def mostrar_produto_mais_caro():
    print()
def mostrar_preco_media():
    print()
def buscar_produto():
    print()

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



while True:

    menu()
    opcao = tratar_erro("Digite uma opção: ")

    if opcao == 1:
        cadastrar_produto(produtos)
    elif opcao == 2:
         print(produtos)
    elif opcao == 3:
        print()
    elif opcao == 4:
        print()
    elif opcao == 5:
        print()
    elif opcao == 6:
        print("Saindo...\n")
        break
    else:
        print("\nOpção inválida!\n")