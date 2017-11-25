from arv_filho_esquerda_irmao_direita import ArvFilhoEsqIrmaoDir
import os
def cls():
    print("\n" * 100)

print( "############################################################")
print("MENU :::: ARVORE N-ARIA :::: FILHO ESQUERDA - IRMAO DIREITA \n")
print("CRIAR ARVORE N- ARIA")
print( "############################################################\n\n")
r = int(input("RAIZ :: "))

raiz = ArvFilhoEsqIrmaoDir()
raiz.criarArvoreNaria(r)

cls()
controle = 9

while(controle != 0 ):
    print( "############################################################")
    print("MENU :::: ARVORE N-ARIA :::: FILHO ESQUERDA - IRMAO DIREITA \n")
    print("1 - INSERIR NO")
    print("2 - EXCLUIR NO")
    print("3 - EXIBIR ARVORE ")
    print("0 - SAIR")
    print( "############################################################\n\n")

    controle = int(input("RESPOSTA:: "))

    #<editor-fold desc="[[  INSERIR  ]]">
    if controle == 1:
        no = int(input("INSERIR EM QUAL NÓ?  "))
        info = int(input("QUAL VALOR?  "))
        retorno = raiz.inserirArvoreNaria(no, info)
        if retorno:
            cls()
            print("INSERIDO COM SUCESSO!!! \n")
            os.system('pause')
            cls()
        else:
            cls()
            print("NAO EXISTE ESSE NO")
            os.system('pause')
            cls()

    if controle == 2:
        no = int(input("EXCLUIR QUAL NO?  "))
        resultado = raiz.excluirNo(no)
        if resultado:
            cls()
            print("EXCLUIDO COM SUCESSO!!! \n")
            os.system('pause')
            cls()
        else:
            cls()
            print("NAO FOI POSSIVEL EXCLUIR O NO")
            os.system('pause')
            cls()

    if controle == 3:
        cls()
        print("ARVORE:: ")
        resultado = raiz.exibirArvoreNaria()
        print("")
        os.system('pause')
        cls()
else:
    print("FALOU!")




