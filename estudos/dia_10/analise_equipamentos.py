equipamentos = [
    {"nome": "Motor A", "potencia": 1500, "temperatura": 65},
    {"nome": "Motor B", "potencia": 2200, "temperatura": 82},
    {"nome": "Motor C", "potencia": 1100, "temperatura": 58},
    {"nome": "Motor D", "potencia": 3000, "temperatura": 91}
]


def equipamentos_criticos(equipamentos):

    i = 0

    criticos = []

    while i < len(equipamentos):

        if equipamentos[i]["temperatura"] > 80 or equipamentos[i]["potencia"] > 2500:
            criticos.append(equipamentos[i]["nome"])
        i += 1

    return criticos

