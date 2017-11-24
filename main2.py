from arv_filho_esquerda_irmao_direita import ArvFilhoEsqIrmaoDir
def cls():
    print("\n" * 100)


'''
r = ArvFilhoEsqIrmaoDir()

r.criarArvoreNaria(0)
r.inserirArvoreNaria(0, 1)
r.inserirArvoreNaria(0, 2)
r.inserirArvoreNaria(0, 3)
r.inserirArvoreNaria(3, 4)
r.inserirArvoreNaria(4, 5)
r.inserirArvoreNaria(3, 6)
r.inserirArvoreNaria(6, 7)
r.inserirArvoreNaria(6, 8)
r.inserirArvoreNaria(7, 9)
r.exibirArvoreNaria()
print("")
r.excluirNo(6)
print("")
r.exibirArvoreNaria()
'''

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
    print("1 - INSEROR NO")
    print("2 - EXCLUIR NO")
    print("0 - SAIR")
    print( "############################################################\n\n")

    controle = int(input("RESPOSTA:: "))

    if controle == 1:
        print("INSERIR EM QUAL NÓ?")
else:
    print("FALOU!")




