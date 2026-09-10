produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 3},
    {"nome": "Sensor", "preco": 250, "estoque": 12},
    {"nome": "Arduino", "preco": 180, "estoque": 8}
]

def menu():
    print("\n1 - Listar produtos")
    print("2 - Adicionar estoque")
    print("3 - Remover estoque")
    print("4 - Alterar preço")
    print("5 - Sair")

def listar_produtos(produtos):
    print("\nListar produtos")
    for produto in produtos:
        print(f"Nome: {produto["nome"]}|Preço: {produto["preco"]}| Estoque: {produto["estoque"]} ")

menu()

while True:    
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        listar_produtos(produtos)
    elif opcao == 2:
        print("Adicionar estoque")
    elif opcao == 3:          
        print("Remover estoque")
    elif opcao == 4:
        print("Alterar preço")
    elif opcao == 5:          
        print("Saindo do programa...\n")
        break
    else:
        print("Opção inválida. Tente novamente.")   



