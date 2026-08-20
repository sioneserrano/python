
alunos = []

def cadastro_vazio():
    print("\n")
    print("Nenhum aluno cadastrado!\n")

def menu():
    print("\n")
    print("1-Cadastrar aluno")
    print("2-Listar alunos")
    print("3-Calcular média")
    print("4-Mostrar aprovado/reprovado")
    print("5-Sair")

def cadastrar_aluno():
    print("\n")
    print("Informe os dados do aluno")
    nome = input("Nome: ")

    nota1 = tratar_erro("Nota 1: ")
    nota2 = tratar_erro("Nota 2: ")

    media = (nota1 + nota2) / 2

    alunos.append({"nome": nome,"nota1": nota1,"nota2": nota2,"media": media})
    print("\nAluno cadastrado com sucesso!\n")

def mostrar_media():
    print("\n")
    print("Média das provas:")
    print("\n")
    i = 0
    while i < len(alunos):
        print(f'{i+1}-Nome: {alunos[i]["nome"]} Média: {alunos[i]["media"]:.1f}')  
        i = i + 1

def listar_alunos():
    if len(alunos) == 0:
        cadastro_vazio()
    else:
        print("\n")
        print("Lista dos alunos:")
        print("\n")
        i = 0
        while i < len(alunos):
            print(f'{i+1}- {alunos[i]["nome"]}')
            i = i + 1

def mostrar_resultado():
    
    if len(alunos) == 0:
        cadastro_vazio()
    else:
        print("\n")
        print("Resultados:")
        print("\n")
        i = 0
        while i < len(alunos):
            
            if alunos[i]["media"] >= 6:
                resultado = "Aprovado"
            else:
                resultado = "Reprovado"

            print(f'{i+1}-Nome: {alunos[i]["nome"]} Média: {alunos[i]["media"]:.1f} Resultado: {resultado}') 
            i = i + 1
    
def tratar_erro(texto):
   while True:
        try:
            numero = int(input(texto))
            return numero
        except ValueError:
            print("Informe um número!")