class Fornecedores:
    def __init__(self,cnpj,nome):
        self.cnpf = cnpj
        self.nome = nome
    def getNome(self):
        return self.nome
    def setNome(self,nome):
        self.nome = nome
    def getCpf(self):
        return self.cnpj
    def setCpf(self,cnpj):
        self.cnpj = cnpj