class Funcionario:
    def __init__(self,cpf,nome,telefone):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
    def getCpf(self):
        return self.cpf
    def setCpf(self,cpf):
        self.cpf = cpf
    def getNome(self):
        return self.nome
    def setNome(self,nome):
        self.nome = nome
    def getTelefone(self):
        return self.telefone
    def setTelefone(self,telefone):
        self.telefone = telefone