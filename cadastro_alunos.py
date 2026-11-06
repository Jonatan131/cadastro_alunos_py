NOTA_MINIMA = 0
NOTA_MAXIMA = 10


def mostrar_menu():
    print("\n>>> Student Registration! <<<")
    print("1 - Add Student")
    print("2 - List All Students")
    print("3 - Search For A Student By Name")
    print("4 - Remove Student")
    print("5 - Overall Average of Grades")
    print("0 - Exit\n")


def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Invalid number! Please type a whole number.")


def ler_nota():
    while True:
        try:
            nota = float(input(f"Enter the student's grade ({NOTA_MINIMA} to {NOTA_MAXIMA}): "))
        except ValueError:
            print("Invalid grade! Please type a number.")
            continue

        if NOTA_MINIMA <= nota <= NOTA_MAXIMA:
            return nota
        print("Student's grade is invalid!")


def ler_nome(mensagem):
    while True:
        nome = input(mensagem).strip()
        if nome:
            return nome
        print("The name cannot be empty!")


def procurar_aluno(alunos, nome_busca):
    for aluno in alunos:
        if aluno["nome"].lower() == nome_busca.lower():
            return aluno
    return None


def mostrar_aluno(aluno):
    print(f"Name: {aluno['nome']} | Age: {aluno['idade']} | Grade: {aluno['nota']:.1f}")


def adicionar_aluno(alunos):
    nome = ler_nome("Enter the student's name: ")
    idade = ler_inteiro("Enter the student's age: ")
    nota = ler_nota()

    aluno = {"nome": nome, "idade": idade, "nota": nota}
    alunos.append(aluno)
    print(f"Student '{nome}' registered successfully!")


def listar_alunos(alunos):
    print("\n>>> List All Students <<<")
    if len(alunos) == 0:
        print("No students registered yet!")
        return

    for posicao, aluno in enumerate(alunos, start=1):
        print(f"{posicao}. ", end="")
        mostrar_aluno(aluno)


def buscar_aluno(alunos):
    print("\n>>> Search For A Student By Name <<<")
    nome_busca = ler_nome("Enter the student's name: ")
    aluno = procurar_aluno(alunos, nome_busca)

    if aluno:
        print("Student Found!")
        mostrar_aluno(aluno)
    else:
        print("Student Not Found!")


def remover_aluno(alunos):
    print("\n>>> Remove a Student <<<")
    nome_busca = ler_nome("Enter the student's name to remove: ")
    aluno = procurar_aluno(alunos, nome_busca)

    if aluno:
        alunos.remove(aluno)
        print(f"Student '{aluno['nome']}' removed successfully!")
    else:
        print("Student Not Found!")


def calcular_media(alunos):
    soma_notas = sum(aluno["nota"] for aluno in alunos)
    return soma_notas / len(alunos)


def mostrar_media(alunos):
    print("\n>>> Overall Average of Grades <<<")
    if len(alunos) == 0:
        print("There are not enough students to calculate the average!")
        return

    print(f"Overall Average = {calcular_media(alunos):.2f}")


def main():
    alunos = []
    opcao = -1

    while opcao != 0:
        mostrar_menu()
        opcao = ler_inteiro("Choose An Option: ")

        match opcao:
            case 1:
                adicionar_aluno(alunos)
            case 2:
                listar_alunos(alunos)
            case 3:
                buscar_aluno(alunos)
            case 4:
                remover_aluno(alunos)
            case 5:
                mostrar_media(alunos)
            case 0:
                print("\n>>> Closing Program <<<")
            case _:
                print("Invalid Option! Please try again.")


if __name__ == "__main__":
    main()
