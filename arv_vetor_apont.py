
class ArvVetorApont(object):
    info = None     #informação a ser armazenada
    filhos = None     #subárvores filhas

    def __init__(self): #cria uma árvore vazia
        self.filhos = []

    def criarArvNaria(self, info):
        self.info = info

    #pesquisa info na arvore
    def estaArvNaria(self, info):
        if (self.info == info):
            return True
        else:
            #percorre pelos filhos e vê se algum possui o valor
            for x in self.filhos:
                if (x.info == info):
                    return True

            #olha os filhos dos filhos
            for x in self.filhos:
                if (x.estaArvNaria(info) == True):
                    return True

            return False

    #retorna subArvore da Arvore
    def subArvoreNaria(self, info):
        if (self.info == info):
            return self
        else:
            #percorre pelos filhos e vê se algum possui o valor
            for x in self.filhos:
                if (x.info == info):
                    return x

            #olha os filhos dos filhos
            for x in self.filhos:
                if (x.subArvoreNaria(info) != None):
                    return x

            return None

    #inserir subarvore como filho de info
    def insereSubArvore(self, subArvore, info):
        sub = self.subArvoreNaria(info)
        if (sub == None):
            return False
        else:
            sub.filhos.append(subArvore)
            return True

    #imprme os filhos
    def listaFilhos(self):
        for x in self.filhos:
            print (x.info)

    #retorna os filhos
    def filhosArvNaria(self):
        return self.filhos

    #retorna se a arvore é vazia
    def vazioArvNaria(self):
        if (self.info == None and len(self.filhos) == 0):
            return True
        else:
            return False

    #imprimir arvore
    def imprimirArvNaria(self):
        print(str(self.info) + " -> ", end="")
        for x in self.filhos:
            print(str(x.info) + " , ", end="")
        print("");

        for x in self.filhos:
            x.imprimirArvNaria()


    def teste (self):
        print ("oi " + self.info)