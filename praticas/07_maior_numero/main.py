
numeros = [10, 1, 11, 20, 100, 3]

def maior_numero(lista):
    maior = lista[0]

    for numero in lista:
        if numero >= maior:
            maior = numero  
    print(f" O maior número da lista é {maior}")

maior_numero(numeros)
