alunos = {}

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite o número de matrícula do aluno: ")
    alunos[matricula] = nome
    print(f"Aluno {nome} adicionado com sucesso!")

def remover_aluno():
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    if matricula in alunos:
        nome = alunos.pop(matricula)
        print(f"Aluno {nome} removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def visualizar_alunos():
    if not alunos:
        print("Nenhum aluno registrado.")
    else:
        print("Lista de alunos:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")

def main():
    while True:
        print("\nOpções:")
        print("1. Adicionar aluno")
        print("2. Remover aluno")
        print("3. Visualizar todos os alunos")
        print("4. Sair")

        opcao = input("Escolha uma opção (1-4): ")

        if opcao == '1':
            adicionar_aluno()
        elif opcao == '2':
            remover_aluno()
        elif opcao == '3':
            visualizar_alunos()
        elif opcao == '4':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
