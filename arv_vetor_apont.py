
class ArvVetorApont(object):
    info = None     #informação a ser armazenada
    filhos = []     #subárvores filhas

    def __init__(self, info):
        self.info = info

    def teste (self):
        print ("oi " + self.info)