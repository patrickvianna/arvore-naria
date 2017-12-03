from arv_vetor_apontador import ArvVetorApont #importamos uma classe
import time

def cls():
    print("\n" * 50)

def print_menu():
    print("---------- MENU ----------")
    print("1. Inserir no na arvore")
    print("2. Remover no da arvore")
    print("3. Exibir arvore")
    print("4. Pesquisa se no pertence a arvore")
    print("5. Destruir arvore")
    print("0. Exit")


if __name__ == "__main__":

    loop = True

    info = input("Digite um valor inicial para árvore:")
    arvPrincipal = ArvVetorApont()
    arvPrincipal.criarArvNaria(info)
    print("Arvore com raiz " + info + " Criada")
    lim = int(input("Digite o limite de filhos que cada nó poderá ter:"))

    while loop:

        if arvPrincipal == None:
            print("Sua arvore foi destruida , o programa terminou!")
            loop = False

        else:

            print_menu()
            opcao = int(input("Escolha uma opcao: "))

            if opcao == 1:

                cls()
                info = input("Digite um valor para adicionar na arvore:")
                print("Novo Nó = " + info)
                noPai = input("Digite o Nó que deseja adicionar como filho este valor:")
                no = ArvVetorApont()
                no.criarArvNaria(info)
                no.infoPai = noPai
                result = arvPrincipal.insereSubArvore(no, noPai, lim)
                if result == 0:
                    print("Erro! Nó pai nao existir.")
                elif result == 1:
                    print("No inserido com sucesso!")
                elif result == 2:
                    print("Erro! Limite de filho estorado, escolha outro no pai.")

            elif opcao == 2:

                cls()
                no = input("Digite o no que quer remover: ")
                if (arvPrincipal.info == no):
                    arvPrincipal = None
                    result = 1
                else:
                    result = arvPrincipal.removerNo(no)
                if result == 0:
                    print("Erro! alguma informacao errada.")
                elif result == 1:
                    print("No removido com sucesso")

            elif opcao == 3:

                cls()
                if arvPrincipal == None:
                    print("Erro, não existe arvore")
                else:
                    arvPrincipal.imprimirArvNaria()

            elif opcao == 4:
                cls()

                info = input("Digite o valor do no para pesquisa:")
                resultado = arvPrincipal.estaArvNaria(info)

                if resultado == True:
                    print("Este no pertence a arvore")
                else:
                    print("Este no nao pertence a arvore")

            elif opcao == 5:
                valor = True
                while valor:
                    escolha = int(input("Tem certeza que quer destrir a arvore: 1 = SIM ou 2 = NAO\nInforme sua opcao!"))

                    if escolha == 1:
                        resultado = arvPrincipal.DestruirArvore()
                        if resultado == True:
                            arvPrincipal = None # destrui a raiz
                            print("Arvore destruida com sucesso!")
                        else:
                            print("Erro ao destruir arvore!")
                        valor = False
                    elif escolha == 2:
                        print("OK")
                        valor = False
                    else:
                        print("Opcao invalida! Digite 1 para Destruir arvore ou 2 para volta ao menu")

            elif opcao == 0:

                cls()
                print('Saindo...')
                loop = False

            else:
                print("Opcao invalida!Escolha novamente.")
