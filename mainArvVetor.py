from arv_vetor_apontador import ArvVetorApont #importamos uma classe
import time

def cls():
    print("\n" * 50)

def print_menu():
    print("---------- MENU ----------")
    print("1. Inserir")
    print("2. Remover")
    print("3. Exibir")
    print("0. Exit")

if __name__ == "__main__":

    loop = True

    info = input("Digite um valor inicial para árvore:")
    arvPrincipal = ArvVetorApont()
    arvPrincipal.criarArvNaria(info)
    print("Arvore com raiz " + info + " Criada")
    lim = int(input("Digite o limite de filhos que cada nó poderá ter:"))

    while loop:
        print_menu()
        opcao = int(input("Escolha uma opcao: "))

        if opcao == 1:

            cls()
            info = input("Digite um valor para adicionar na arvore:")
            print("Novo Nó = " + info)
            noSubArvore = input("Digite o Nó que deseja adicionar como filho este valor:")
            no = ArvVetorApont()
            no.criarArvNaria(info)
            result = arvPrincipal.insereSubArvore(no, noSubArvore, lim)
            if result == 0:
                print("Erro! Nó pai nao existir.")
            elif result == 1:
                print("No inserido com sucesso!")
            elif result == 2:
                print("Erro! Limite de filho estorado, escolha outro no pai.")

        elif opcao == 2:

            cls()
            noFilho = input("Digite o no que quer remover: ")
            noPai = input("Digite o pai do nó que quer remover: ")
            result = arvPrincipal.removerNo(noPai,noFilho)
            if result == 0:
                print("Erro! alguma informacao errada.")
            elif result == 1:
                print("No removido com sucesso")

        elif opcao == 3:

            cls()
            arvPrincipal.imprimirArvNaria()

        elif opcao == 0:

            cls()
            print('Saindo...')
            loop = False

        else:
            print("Opcao invalida!Escolha novamente.")
