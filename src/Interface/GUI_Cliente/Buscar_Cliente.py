from tkinter import *
from Entidades.Controle import ControladorCliente


class Busca_cliente:
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

        self.titulo = Label(self.primeiroContainer, text="Buscar Cliente")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.cpfLabel = Label(self.segundoContainer, text="CPF", font=self.fontePadrao)
        self.cpfLabel.pack(side=LEFT)

        self.cpf = Entry(self.segundoContainer)
        self.cpf["width"] = 30
        self.cpf["font"] = self.fontePadrao
        self.cpf.pack(side=LEFT)

        self.buscar = Button(self.terceiroContainer)
        self.buscar["text"] = "Buscar"
        self.buscar["font"] = ("Calibri", "8")
        self.buscar["width"] = 12
        self.buscar["command"] = self.validar_dados
        self.buscar.pack()

        self.mensagem = Label(self.terceiroContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.nomeLabel = Label(self.quartoContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.quartoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

    def validar_dados(self):  # valida os campos, se todos estiverem ok, inserir normalmente no arquivo
        if self.cpf.get() == "":
            self.mensagem["text"] = "CPF vazio, por favor informe um CPF"
        else:
            cpf = self.cpf.get()
            resposta = ControladorCliente.buscar_Cliente(cpf)
            if isinstance(resposta,str):
                self.mensagem["text"] = resposta
            else:
                self.mensagem["text"] = ''
                self.nome.delete(0,END)
                self.nome.insert(0,resposta.getNome())


