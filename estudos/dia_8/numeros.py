numeros = [2, 9, 1, 30, 10, 10]

def soma_numeros(lista):

    soma = 0
    for numero in lista:
        soma = soma + numero
    return soma 

def maior_numero(lista):

    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

def numero_de_pares(lista):

    pares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares = pares + 1
    return pares

print(f"\nLista: {numeros}")
print(f"\nSoma dos números da lista: {soma_numeros(numeros)}")
print(f"Maior número da lista: {maior_numero(numeros)}")
print(f"Quantidade de pares na lista: {numero_de_pares(numeros)}\n")