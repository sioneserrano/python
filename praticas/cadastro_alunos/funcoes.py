
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
    print("5-Melhor Aluno")
    print("6-Estatística da turma")
    print("7-Sair")

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
    if len(alunos) != 0:

        print("\n")
        print("Média das provas:")
        print("\n")
        i = 0
        while i < len(alunos):
            print(f'{i+1}-Nome: {alunos[i]["nome"]} Média: {alunos[i]["media"]:.1f}')  
            i = i + 1
    else:
        cadastro_vazio()
        
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
    
def posicao_melhor():
    if len(alunos) != 0:
    
        i=0
        melhor = alunos[0]["media"]
        while i < len(alunos):

            if alunos[i]["media"] > melhor:
                melhor = alunos[i]["media"]
                indice = i
            i=i+1
        return indice
    else:
        cadastro_vazio()

posicao = posicao_melhor()

def melhor_aluno(posicao):
    if len(alunos) != 0:
        print("\nMelhor(es) Aluno(s)\n")
        print(f'Nome: {alunos[posicao]["nome"]} Média: {alunos[posicao]["media"]:.1f}') 
    else:
        cadastro_vazio()

def estatistica_turma(alunos):

    num_alunos = len(alunos)
    soma_medias = 0
    num_aprovados = 0
    num_reprovados = 0

    i=0
    while i < num_alunos:

        soma_medias = soma_medias + alunos[i]["media"]

        if alunos[i]["media"] >= 6:
            num_aprovados = num_aprovados + 1
        else:
            num_reprovados = num_reprovados + 1
        i=i+1

    if num_alunos !=0:
        media_turma = soma_medias/num_alunos
        print("\nEstatística da turma\n")
        print(f"Alunos cadstrados: {num_alunos} \nMédia da turma: {media_turma:.2f} \nAprovados: {num_aprovados} \nReprovadsos: {num_reprovados}")
    else:
        cadastro_vazio()

def tratar_erro(texto):
   while True:
        try:
            numero = int(input(texto))
            return numero
        except ValueError:
            print("Informe um número!")