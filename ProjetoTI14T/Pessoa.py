class Pessoa:
    def __init__(self): #método construtor
        self.nome = ""
        self.telefone = ""
        self.endereco = ""

    #métodos de acesso gets e sets
    def getNome(self):
        return self.nome

    def getTelefone(self):
        return self.telefone

    def getEndereco(self):
        return self.endereco

    def setNome(self, nome):
        self.nome = nome

    def setTelefone(self, telefone):
        self.telefone = telefone

    def setEndereco(self, endereco):
        self.endereco = endereco

    #cadastrar
    def cadastrar(self, nome, telefone, endereco):
        self.setNome(nome)
        self.setTelefone(telefone)
        self.setEndereco(endereco)

    def consultarTudo(self):
        return "nome: {}\n" "telefone: {}\n" "endereço: {}".format(self.getNome(), self.getTelefone(), self.getEndereco())

