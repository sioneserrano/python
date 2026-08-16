from funcoes import * 

while True:
    menu()
    opcao = int(input("Informe uma opcao: "))
    
    if opcao == 1:
      cadastrar_aluno()

    elif opcao == 2:
      listar_alunos()

    elif opcao == 3:
      mostrar_media()

    elif opcao == 4:
      mostrar_resultado()

    elif opcao == 5:
      print("Saindo...")
      break
    else:
      print("Opção inválida!\n")