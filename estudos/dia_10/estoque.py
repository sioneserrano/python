produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 3},
    {"nome": "Sensor", "preco": 250, "estoque": 12},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2},
    {"nome": "Inversor", "preco": 2100, "estoque": 5}
]


def verificar_estoque(produtos):

    estoque_abaixo = []
    estoque_normal = []

    for produto in produtos:
        if produto["estoque"] < 5:
            estoque_abaixo.append(produto["nome"])

        elif produto["estoque"] >= 5:
            estoque_normal.append(produto["nome"])
        

    return {"normal": estoque_normal, "abaixo": estoque_abaixo}


def mostrar_estoque(produtos):

    estoque = verificar_estoque(produtos)

    print("\nProdutos com estoque normal:")
    for i in estoque['normal']:
        print(i)

    print("\nProdutos com estoque baixo:")
    for i in estoque['abaixo']:
        print(i)
    print("\n\n")
    
mostrar_estoque(produtos)
    