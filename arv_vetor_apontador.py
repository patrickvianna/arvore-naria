
class ArvVetorApont(object):
    info = None     #informação a ser armazenada
    filhos = None     #subárvores filhas
    limite = 0        #limite de filhos
    infoPai = None    #atributo para ter uma referencia do pai

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
        print("")

        for x in self.filhos:
            x.imprimirArvNaria()

    #remover subArvore
    def removerNo(self,noRemover):
        no = self.subArvoreNaria(noRemover) #Busca o no a ser removido
        pai = self.subArvoreNaria(no.infoPai) #Busca o pai do no a ser removido

        if no == None: #Se no a remover for null retorna 0
            return 0
        else:
            if (pai is not None):
                pai.filhos.remove(no) #removo da lista de filho do pai a subArvore no e retorno 1
            return 1

    def DestruirArvore(self):

        i = 0
        while i < len(self.filhos): #remover todos os filho da raiz
            self.filhos.pop()

        if len(self.filhos) == 0: #se a raiz tive 0 filhos retorna true se nao false
            return True
        else:
            return False
