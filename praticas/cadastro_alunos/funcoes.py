
alunos = []

def menu():
    print("\n")
    print("1-Cadastrar aluno")
    print("2-Listar alunos")
    print("3-Calcular média")
    print("4-Mostrar aprovado/reprovado")
    print("5-Sair")
    print("\n")

def cadastrar_aluno():
    print("\n")
    print("Informe os dados do aluno")
    nome = input("Nome: ")

    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))

        media = (nota1 + nota2) / 2
    
        aluno = {
            "nome": nome,
            "nota1": nota1,
            "nota2": nota2,
            "media": media 
        }
        alunos.append(aluno)
        print("\nAluno cadastrado com sucesso!\n")
    except ValueError:
        print("As medias devem ser numero!")
    
 
    
def mostrar_media():
    print("\n")
    print("Média das provas:")
    i = 0
    while i < len(alunos):
        print(f'{i+1}- {alunos[i]["nome"]}') 
        print(f'Média: {alunos[i]["media"]:.1f}\n')  
        i = i + 1
    print("\n")

def listar_alunos():
    if len(alunos) == 0:
        print("\n")
        print("Nenhum aluno cadastrado!\n")
    else:
        print("\n")
        print("Lista dos alunos:")
        i = 0
        while i < len(alunos):
            print(f'{i+1}- {alunos[i]["nome"]}')
            i = i + 1
        print("\n")

def mostrar_resultado():
    print("\n")
    print("Resultados:")
    i = 0
    while i < len(alunos):
        
        print(f'{i+1}- {alunos[i]["nome"]}') 
        print(f'Média: {alunos[i]["media"]:.1f}')
        
        if alunos[i]["media"] >= 6:
            print("Aprovado")
        else:
            print("Reprovado")
        print("")
        i = i + 1
    print("\n")

def tratar_erro(texto)
   while True:
        try:
            numero = int(input(texto))
            return numero
        except ValueError:
            print("Informe um número!")