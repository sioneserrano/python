
def tratar_erro(texto):
    while True:   
        try:
            idade = int(input(texto))
            if idade >= 0:
                return idade
            else:
                print("A idade tem que ser maior ou igual que zero!")
                
        except ValueError:
            print("A idade tem que ser um numero!")

idade = tratar_erro("Informe a sua idade: ")

print(f"Sua idade: {idade}")


