produto = {
    "nome": "Motor",
    "preco": 1500,
    "estoque": 3
}


def atualizar_preco(produto):

    preco = float(input("Digite o novo preço: "))
    produto["preco"] = preco

    return produto


print(atualizar_preco(produto))

print(f"Novo preço: {produto["preco"]}")