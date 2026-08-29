produtos = []


def cadastrar_produto():
    print()
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
            numero = int(input(texto))
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
        print()
    elif opcao == 2:
        print()
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