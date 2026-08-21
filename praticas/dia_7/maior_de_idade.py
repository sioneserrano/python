
pessoas = [{"nome": "Sione", "idade": 22}, {"nome": "Araujo", "idade": 18}, 
           {"nome": "Maria", "idade": 24}, {"nome": "João", "idade": 15}, {"nome": "Atanásio", "idade": 4}]

def maiores(pessoas):
    maiores = []
    i=0
    while i < len(pessoas):
        if pessoas[i]['idade'] >= 18:
            maiores.append(pessoas[i])
        i=i+1
    return maiores

maiores = maiores(pessoas)

def mostrar_maiores(maiores):
    i=0
    print("\nMaiores de idade\n")
    while i < len(maiores):
        print(f"{i+1}-Nome: {maiores[i]['nome']} Idade: {maiores[i]['idade']} anos")
        i=i+1

mostrar_maiores(maiores)