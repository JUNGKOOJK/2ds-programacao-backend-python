


# for loop com if (condicional)
sucesso = False
for numero in range(3):
    print("Tentativa")
    if sucesso: # Dentro da variável 'sucesso' está o valor booleano (True ou False)
        print("Sucesso, meu jovem.")
        break
else:
    print("Todas as 3 tentativas falharam!!!")    