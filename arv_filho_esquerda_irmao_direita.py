class ArvFilhoEsqIrmaoDir:
    # region atributos
    info = None
    filhoEsq = None
    irmaoDir = None

    # endregion

    # Em todas as funções, self é a raiz

    #region [[  CONSTRUTOR  ]]
    def __init__(self):
        self.filhoEsq = None
        self.irmaoDir = None
        self.info = None
    #endregion
    # region [[  CRIA  ]]
    def criarArvoreNaria(self, info):
        self.filhoEsq = None
        self.irmaoDir = None
        self.info = info

    # endregion
    # region [[  INSERE  ]]
    def inserirArvoreNaria(self, noPai, novaChave):
        pai = self.buscarNo(noPai)
        if pai is None: return False
        filho = ArvFilhoEsqIrmaoDir()
        filho.criarArvoreNaria(novaChave)
        p = pai.filhoEsq
        if (p == None):
            pai.filhoEsq = filho
        else:
            while (p.irmaoDir):
                p = p.irmaoDir
            p.irmaoDir = filho
        return True

    # endregion
    # region [[  BUSCAR  ]]
    def buscarNo(self, no):
        if self is None: return
        if self.info == no: return self
        p = self.filhoEsq
        while p:
            resp = p.buscarNo(no)
            if resp: return resp
            p = p.irmaoDir
        return None

    # endregion
    #region [[  EXIBIR  ]]
    def exibirArvoreNaria(self):
        if self is None: return False
        print(str(self.info) + "(", end="")
        p = self.filhoEsq
        while p:
            p.exibirArvoreNaria()
            p = p.irmaoDir
        print(") ", end="")
        return True


    #endregion
    # region [[  EXCLUIR NO  ]]
    def excluirNo(self, no):
        if self is None: return False
        excluido = self.buscarNo(no)
        if excluido is None:
            return False
        else:
            excluido = excluido.excluirFilhosNo()
            return True

        return

    #endregion

    #region [[  EXCLUIR FILHOS  ]]
    def excluirFilhosNo(self):
        if (self.filhoEsq is not None):
            print("Pai:" + str(self.info) + " - Filho:" + str(self.filhoEsq.info))
            self.filhoEsq = self.filhoEsq.excluirFilhosNo()

        if (self.irmaoDir is not None):
            print("Pai:" + str(self.info) + " - Irmao:" + str(self.irmaoDir.info))
            self.v = self.irmaoDir.excluirFilhosNo()

        return None


    #endregion
