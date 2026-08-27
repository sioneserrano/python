numeros = [12, 5, 8, 21, 4, 17, 10]

def analisar_numeros(numeros):

    maior = numeros[0]
    menor = numeros[0]
    num_pares = 0
    num_impares = 0


    for numero in numeros:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
        if numero % 2 == 0:
            num_pares = num_pares + 1
        else:
            num_impares = num_impares + 1
    return {"Maior": maior , "Menor": menor , "Pares": num_pares , "Impares": num_impares}


analise = analisar_numeros(numeros)

def mostrar_analise(analise):

    print("\nAnálise dos números\n")
    for key, value in analise.items():
        print(f"{key}: {value}")
    print("\n\n")

mostrar_analise(analise)