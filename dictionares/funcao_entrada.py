pokemon = {}


def ler_float(mensagem):
  while True:
    try:
        return float(input(mensagem))
    except ValueError:
        print("Porfavor, animal, digite umnúmero válido")


def cadastrar(alunos):
    nome = input("Nome:").strip().title()
    nota = ler_float("Nota: ")
    alunos[nome] = {"nota": nota}


cadastrar(pokemon)
print(pokemon)