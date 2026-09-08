produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 3},
    {"nome": "Sensor", "preco": 250, "estoque": 12},
    {"nome": "Arduino", "preco": 180, "estoque": 8}
]



while True:

    print("1 - Listar produtos")
    print("2 - Adicionar estoque")
    print("3 - Remover estoque")
    print("4 - Alterar preço")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Listar produtos")
    elif opcao == 2:
        print("Adicionar estoque")
    elif opcao == 3:          
        print("Remover estoque")
    elif opcao == 4:
        print("Alterar preço")
    elif opcao == 5:          
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")    



