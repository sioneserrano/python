
temperaturas = [20, 25, 30, 35, 40]

def converter_temperaturas(temperaturas):

    for i, temperatura in enumerate(temperaturas):
        temperaturas[i] = (temperatura * (9/5)) + 32
    return temperaturas

temperatura_em_f = converter_temperaturas(temperaturas)

print("Lista modificada:", temperatura_em_f)
