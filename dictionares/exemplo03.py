#Sintaxe correta:entrada pode falhar
#Erro de sintaxe
try:
 idade = int(input("Idade: "))
except ValueError:
   print("Digite um número inteiro.")

if idade >= 15:
    print ("Maior")