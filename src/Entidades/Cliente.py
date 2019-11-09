class Cliente:
    def __init__(self,cpf,nome):
        self.cpf = cpf
        self.nome = nome
    def getNome(self):
        return self.nome
    def setNome(self,nome):
        self.nome = nome
    def getCpf(self):
        return self.cpf
    def setCpf(self,cpf):
        self.cpf = cpf