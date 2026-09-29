opcao = input("Escolha 1,2 ou 3:")

match opcao
    case "1":
        print("Iniciar Jogo")
    case "2":
        print("Ver Instruções")
    case "3":
        print("Sair")
    case _:
        print("")