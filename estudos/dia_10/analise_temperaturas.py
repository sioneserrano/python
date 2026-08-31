temperaturas = [23.5, 25.1, 27.8, 30.2, 28.4, 21.9, 26.7]

def analisar_temperaturas(temperaturas):

    maxima = temperaturas[0]
    minima = temperaturas[0]
    soma = 0
    acima_de_27 = 0

    for temperatura in temperaturas:

        soma += temperatura

        if temperatura > maxima:
            maxima = temperatura
        if temperatura < minima:
            minima = temperatura
        if temperatura > 27:
            acima_de_27 += 1
    
    media = soma/len(temperaturas)
    return {"Maxima": maxima,"Minima": minima,"Media": media,"Temperaturas acima de 27": acima_de_27}
    

def mostrar_analise(temperaturas):

    analise = analisar_temperaturas(temperaturas)

    print("\n\nAnalise das temperaturas\n")
    for key, value in analise.items():
        print(f"{key}: {value}")
    print("\n\n")


mostrar_analise(temperaturas)