from tkinter import *
from Entidades.Controle import ControladorFuncionario


class Busca_func:
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

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Buscar Funcionário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.cpfLabel = Label(self.segundoContainer, text="CPF", font=self.fontePadrao)
        self.cpfLabel.pack(side=LEFT)

        self.cpf = Entry(self.segundoContainer)
        self.cpf["width"] = 30
        self.cpf["font"] = self.fontePadrao
        self.cpf.pack(side=LEFT)

        self.deletar = Button(self.terceiroContainer)
        self.deletar["text"] = "Buscar"
        self.deletar["font"] = ("Calibri", "8")
        self.deletar["width"] = 12
        self.deletar["command"] = self.validar_dados
        self.deletar.pack()

        self.mensagem = Label(self.terceiroContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.nomeLabel = Label(self.quartoContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.quartoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.telefoneLabel = Label(self.quintoContainer, text="Telefone", font=self.fontePadrao)
        self.telefoneLabel.pack(side=LEFT)

        self.telefone = Entry(self.quintoContainer)
        self.telefone["width"] = 30
        self.telefone["font"] = self.fontePadrao
        self.telefone.pack(side=LEFT)

    def validar_dados(self):  # valida os campos, se todos estiverem ok, inserir normalmente no arquivo
        if self.cpf.get() == "":
            self.mensagem["text"] = "CPF vazio, por favor informe um CPF"
        else:
            cpf = self.cpf.get()
            resposta = ControladorFuncionario.buscar_Funcionario(cpf)
            if isinstance(resposta,str):
                self.mensagem["text"] = resposta
            else:
                self.mensagem["text"] = ''
                self.telefone.delete(0,END)
                self.telefone.insert(0,resposta.getTelefone())
                self.nome.delete(0,END)
                self.nome.insert(0,resposta.getNome())


