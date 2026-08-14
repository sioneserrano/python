alunos = []

while True:

    print("1-Cadastrar aluno")
    print("2-Listar alunos")
    print("3-Cálcular média")
    print("4-Mostrar aprovado/reprovado")
    print("5-Sair")
   
    print("\n")
    opcao = int(input("Informe uma opção: "))
    
    print("\n")

    if opcao == 1:

        print("Informe os dados do aluno")
       
        nome = input("Nome: ")
       
        nota1 = float(input("Nota 1: "))
       
        nota2 = float(input("Nota 2: "))


        media = (nota1 + nota2)//2

        print("\n")
       
        aluno = {
            "nome": nome,
            "nota1": nota1,
            "nota2": nota2,
            "media": media 
        }
       
        alunos.append(aluno)
       
    elif opcao == 2:
        print("Lista dos alunos")
        #print(alunos)

        i = 0
        while i < len(alunos):
          print(f"{i+1}- {alunos[i]["nome"]}")  #(???)
          i=i+1

        print("\n")
             
    elif opcao == 3:

        print("Média das provas")
        print("")

        i = 0
        while i < len(alunos):
          print(f"{i+1}- {alunos[i]["nome"]}")  #(???)
          print(f"Média:{alunos[i]["media"]}\n")
          i=i+1

        print("\n")

        
    elif opcao == 4:
        
        print("Resultados")
        print("")

        i = 0
        while i < len(alunos):
          print(f"{i+1}- {alunos[i]["nome"]}")  #(???)
          print(f"Média:{alunos[i]["media"]}")

          if alunos[i]["media"] >=6:
            print("Aprovado")
          else:
            print("Reprovado")
          i=i+1
          print("\n")

    elif opcao == 5:
        break
    else:
        print("Opção invalida!")