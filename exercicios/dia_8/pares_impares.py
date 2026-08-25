numeros = [12, 11, 10, 5, 16, 6]

def separar_numero(lista):

    pares = []
    impares = []

    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    return {"pares": pares, "impares": impares}

separados = separar_numero(numeros)

print(f"\nPares: {separados['pares']}")
print(f"Impares: {separados['impares']}\n")