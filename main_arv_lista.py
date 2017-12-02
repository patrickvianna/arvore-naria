from arv_lista import ArvLista #importamos uma classe
import time

def cls():
    print("\n" * 50)

def print_menu():
    print("---------- MENU ----------")
    print("1. Inserir")
    print("2. Remover")
    print("3. Exibir")
    print("4. Esta na arvore")
    print("5. Limpar arvore")
    print("0. Exit")

if __name__ == "__main__":

    loop = True

    info = input("Digite um valor inicial para árvore:")
    arvPrincipal = ArvLista()
    arvPrincipal.criarArvNaria(info)
    print("Arvore com raiz " + info + " Criada")

    while loop:
        print_menu()
        opcao = int(input("Escolha uma opcao: "))

        if opcao == 1:

            cls()
            info = input("Digite um valor para adicionar na arvore:")
            print("Novo Nó = " + info)
            if (arvPrincipal == None):
                arvPrincipal = ArvLista()
                arvPrincipal.criarArvNaria(info)
                print("No inserido com sucesso!")
            else:
                noSubArvore = input("Digite o Nó que deseja adicionar como filho este valor:")
                no = ArvLista()
                no.criarArvNaria(info)
                result = arvPrincipal.insereSubArvore(no, noSubArvore)
                if result == False:
                    print("Erro! No pai nao existe.")
                elif result == True:
                    print("No inserido com sucesso!")

        elif opcao == 2:

            cls()
            noRemover = input("Digite o no que quer remover: ")
            if (arvPrincipal.info == noRemover):
                arvPrincipal = None
            else:
                result = arvPrincipal.removerNo(noRemover)
                if result == False:
                    print("Erro! alguma informacao errada.")
                elif result == True:
                    print("No removido com sucesso")
            print("No removido com sucesso")

        elif opcao == 3:

            cls()
            if (arvPrincipal == None):
                print("A arvore esta vazia")
            else:
                arvPrincipal.imprimirArvNaria()

        elif opcao == 4:
            cls()
            info = input("Digite um valor que deseja pesquisar na arvore:")
            if (arvPrincipal.estaArvNaria(info) == True):
                print ("TRUE - Este no esta na arvore!    =)")
            else:
                print ("FALSE - Este no NAO esta na arvore!   =(")

        elif opcao == 5:
            cls()
            arvPrincipal.removerNo(arvPrincipal.info)
            arvPrincipal = None

        elif opcao == 0:

            cls()
            print('Saindo...')
            loop = False

        else:
            print("Opcao invalida!Escolha novamente.")
