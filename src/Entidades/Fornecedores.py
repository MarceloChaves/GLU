class Fornecedores:
    def __init__(self,cnpj,nome):
        self.cnpf = cnpj
        self.nome = nome
    def getNome(self):
        return self.nome
    def setNome(self,nome):
        self.nome = nome
    def getCnpj(self):
        return self.cnpj
    def setCnpj(self,cnpj):
        self.cnpj = cnpj