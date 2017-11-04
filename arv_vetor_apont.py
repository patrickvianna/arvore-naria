
class ArvVetorApont(object):
    info = None     #informação a ser armazenada
    filhos = None     #subárvores filhas

    def __init__(self, info): #cria uma árvore vazia
        self.info = info
        self.filhos = []

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


    #imprme os filhos
    def listaFilhos(self):
        for x in self.filhos:
            print (x.info)

    #retorna a subarvore
    def subArvNaria(self):
        return self.filhos

    #retorna se a arvore é vazia
    def vazioArvNaria(self):
        if (self.info == None and len(self.filhos) == 0):
            return True
        else:
            return False


    def teste (self):
        print ("oi " + self.info)