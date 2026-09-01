produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 3},
    {"nome": "Sensor", "preco": 250, "estoque": 12},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2},
    {"nome": "Inversor", "preco": 2100, "estoque": 5}
]


def produtos_caros(produtos):

    filtragem = []

    for produto in produtos:
        if produto["preco"] > 1000:
            filtragem.append(produto["nome"])

    return filtragem


def mostrar_filtragem(produtos):

    filtragem = produtos_caros(produtos)

    print(f"\n\nProdutos com preço superior a R$ 1.000:")
    for produto in filtragem:
        print(produto)
    print("\n\n")

mostrar_filtragem(produtos)
    