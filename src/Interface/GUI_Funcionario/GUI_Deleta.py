from tkinter import *
from Entidades.Controle import ControladorFuncionario


class Deleta_func:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Deletar Funcionário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.cpfLabel = Label(self.segundoContainer, text="CPF", font=self.fontePadrao)
        self.cpfLabel.pack(side=LEFT)

        self.cpf = Entry(self.segundoContainer)
        self.cpf["width"] = 30
        self.cpf["font"] = self.fontePadrao
        self.cpf.pack(side=LEFT)

        self.deletar = Button(self.terceiroContainer)
        self.deletar["text"] = "Deletar"
        self.deletar["font"] = ("Calibri", "8")
        self.deletar["width"] = 12
        self.deletar["command"] = self.validar_dados
        self.deletar.pack()

        self.mensagem = Label(self.terceiroContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def validar_dados(self):  # valida os campos, se todos estiverem ok, inserir normalmente no arquivo
        if self.cpf.get() == "":
            self.mensagem["text"] = "CPF vazio, por favor informe um CPF"
        else:
            cpf = self.cpf.get()
            resposta = ControladorFuncionario.deletar_Funcionario(cpf)
            if resposta == 'O cpf informado é inválido!':
                self.mensagem["text"] = resposta
            elif resposta == 'Funcionário não encontrado':
                self.mensagem["text"] = resposta
            elif resposta == 'Deletado com Sucesso':
                self.mensagem["text"] = resposta
