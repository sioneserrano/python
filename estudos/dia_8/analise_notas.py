
notas = []

def menu():

    print("\n1.Adicionar nota")
    print("2.Listar notas ")
    print("3.Mostrar maior nota")
    print("4.Mostrar media")
    print("5.Mostrar quantidade de aprovados")
    print("6.Sair")

def tratar_erro(texto):

    while True:
        try:
            numero = int(input(texto))
            return numero
        except ValueError:
            print("A opcao tem que ser um número!")


def tratar_nota(texto):

    while True:
        try:
            nota = int(input(texto))
            if nota >= 0 and nota <= 10:
                return nota
            else:
                print("Informe uma nota entre 0 e 10!")
        except ValueError:
            print("A nota tem que ser um número!")


def mostrar_notas(notas):

    print("\nLista das notas")
    for i, nota in enumerate(notas):
        print(f"Nota {i+1}: {nota}")
    print("\n")

def maior_nota(notas):

    print("\nMaior nota")
    maior = notas[0]
    indice = 0
   
    for i, nota in enumerate(notas):
        if nota > maior:
            maior = nota
            indice = i
    print(f"Nota {indice+1}: {nota}\n")

def media_notas(notas):

    print("\nMedia das notas")
    soma = 0
    for nota in notas:
        soma = soma + nota
    media = soma/len(notas)
    print(f"A media das notas é {media:.2f}\n")

def numero_aprovados(notas):

    print("\nQuantiade de aprovados")
    aprovados = 0
    for nota in notas:
        if nota >=6:
            aprovados = aprovados + 1
    print(f"Número de aprovados: {aprovados}\n")

def cadastro_vazio():
    print("Cadastro vazio!")

while True:

    menu()
    opcao = tratar_erro("Digite uma opção: ")

    if opcao == 1:
        nota = tratar_nota("\nDigite a nota: ")
        print("Nota cadastrada!")
        notas.append(nota)

    elif opcao == 2:
        if len(notas) == 0:
            cadastro_vazio()
        else:
            mostrar_notas(notas)
            print()
    elif opcao == 3:
        if len(notas) == 0:
            cadastro_vazio()
        else:
            maior_nota(notas)

    elif opcao == 4:

        if len(notas) == 0:
            cadastro_vazio()
        else:
            media_notas(notas)

    elif opcao == 5:
        if len(notas) == 0:
            cadastro_vazio()
        else:
            numero_aprovados(notas)
    elif opcao == 6:
        print("Saindo...\n")
        break
    else:
        print("Opcao invalida!")