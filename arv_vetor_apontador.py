
class ArvVetorApont(object):
    info = None     #informação a ser armazenada
    filhos = None     #subárvores filhas
    limite = 0        #limite de filhos

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

    #retorna subArvore da Arvore com informação = info
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
                subSubArvore = x.subArvoreNaria(info)
                if (subSubArvore != None):
                    return subSubArvore

            return None

    #inserir subarvore como filho de info
    def insereSubArvore(self, subArvore, info, lim):
        sub = self.subArvoreNaria(info)
        if (sub == None):
            return 0
        else:
            if sub.limite < lim:  #se limite do no pai for menor que 4 ele adiciona o filho
                sub.filhos.append(subArvore)
                sub.limite += 1  #incrementa o valor do limite do no pai
                return 1
            else:
                return 2


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

    #remover subArvore
    def removerNo(self,noPai,noRemover):
        pai = self.subArvoreNaria(noPai) #Busca o pai
        filho = self.subArvoreNaria(noRemover) #Busca o no a remover
        if pai == None or filho == None: #Se pai ou o no a remover for null retorna 0
            return 0
        else:
            pai.filhos.remove(filho) #removo da lista de filho do pai a subArvore filho e retorno 1
            return 1