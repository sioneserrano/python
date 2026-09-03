produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 3},
    {"nome": "Sensor", "preco": 250, "estoque": 12},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]


def alterar_preco(produtos):

    nome_produto = input("Digite o nome do produto: ")

    for produto in produtos:
        
        if produto["nome"] == nome_produto:
           preco = float(input("Informe um novo preço: "))

           produto["preco"] = preco

    return produtos
            
print(alterar_preco(produtos))