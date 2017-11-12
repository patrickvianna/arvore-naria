from arv_vetor_apont import ArvVetorApont #importamos uma classe
import time

def cls():
    print("\n" * 100)

if __name__ == "__main__":
    subArvore = None
    arvPrincipal = None
    acaoPrincipal = ""
    #interface
    while (acaoPrincipal != "0"):
        cls()
        acoes = ["Árvore Pincipal", "Sub-arvore"]
        cont = 1;
        #imprime o menu
        print("Menu:")
        for x in acoes:
            print(str(cont) + " - " + x)
            cont += 1
        acaoPrincipal = input("Digite (0 para sair):")
        print (acaoPrincipal)


        #arvore principal
        if (acaoPrincipal == "1"):
            cls()
            acao = ""
            while (acao != "0"):
                acoes = ["Criar arvore principal vazia", "Criar arvore principal com valor inicial",
                         "Imprimir arvore principal",
                         "Inserir Sub-arvore no nó X da árvore principal"]
                cont = 1;
                # imprime o menu
                print("Menu:")
                for x in acoes:
                    print(str(cont) + " - " + x)
                    cont += 1
                acao = input("Digite (0 para voltar):")
                print(acao)



                if (acao == "1"):
                    cls()
                    arvPrincipal = ArvVetorApont()
                    print("Arvore Vazia Criada")
                    time.sleep(2)

                elif (acao == "2"):
                    cls()
                    info = input("Digite um valor inicial para árvore:")
                    arvPrincipal = ArvVetorApont()
                    arvPrincipal.criarArvNaria(info)
                    print("Arvore com raiz " + info + " Criada")
                    time.sleep(2)

                elif (acao == "3"):
                    cls()
                    arvPrincipal.imprimirArvNaria()

                elif (acao == "4"):
                    cls()
                    if (subArvore == None):
                        print ("Crie uma subarvore primeiro!")
                    else:
                        no = input ("Digite em qual nó deseja inserir a sub-arvore:")
                        if (arvPrincipal.insereSubArvore(subArvore, no) == True):
                            print("Sub-arvore inserida com sucesso. Imprima para você ver!")
                            subArvore = None
                        else:
                            print ("Nao foi encontrado esse nó na árvore principal!")
                    time.sleep(2)




        #subarvore
        elif (acaoPrincipal == "2"):
            acoes = ["Criar subarvore com valor inicial", "Inserir nó X como filho do nó Y", "Imprimir sub-arvore"]
            # imprime o menu

            cls()
            acao = ""
            while (acao != "0"):
                cont = 1
                print("Menu:")
                for x in acoes:
                    print(str(cont) + " - " + x)
                    cont += 1
                acao = input("Digite (0 para voltar):")

                if (acao == "1"):
                    cls()
                    info = input("Digite um valor inicial para árvore:")
                    subArvore = ArvVetorApont()
                    subArvore.criarArvNaria(info)
                    print("Sub Arvore com raiz " + info + " Criada")
                    time.sleep(2)

                elif (acao == "2"):
                    cls()
                    info = input ("Digite um valor para adicionar na subarvore:")
                    print("Novo Nó = " + info)
                    noSubArvore = input("Digite o Nó que deseja adicionar como filho este valor:")
                    no = ArvVetorApont()
                    no.criarArvNaria(info)
                    if (subArvore.insereSubArvore(no, noSubArvore) == True):
                        print("Sub-arvore inserida com sucesso. Imprima para você ver!")
                    else:
                        print("Nao foi encontrado esse nó!")
                    time.sleep(2)
                    no = None

                elif (acao == "3"):
                    cls()
                    subArvore.imprimirArvNaria()




#TESTANDO INSERIR NA ARVORE
'''
    arv = ArvVetorApont() #instancia o objeto
    arv.criarArvNaria(1)
    arv2 = ArvVetorApont()
    arv2.criarArvNaria(2)
    arv3 = ArvVetorApont()
    arv3.criarArvNaria(3)
    arv4 = ArvVetorApont()
    arv4.criarArvNaria(4)
    arv5 = ArvVetorApont()
    arv5.criarArvNaria(5)
    arv6 = ArvVetorApont()
    arv6.criarArvNaria(6)

    arv3.filhos.append(arv4)
    arv3.filhos.append(arv5)

    arv.filhos.append(arv2)
    arv.filhos.append(arv3)

    #arv.insereSubArvore(arv3, 1)
    arv.insereSubArvore(arv6, 5)
    #arv.subArvoreNaria(3).imprimirArvNaria()
    arv.imprimirArvNaria()
'''