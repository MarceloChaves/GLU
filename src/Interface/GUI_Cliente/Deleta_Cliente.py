from tkinter import *
from Entidades.Controle import ControladorCliente
from Entidades.Controle import ControladorSuperADM


class Deleta_cliente:
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

        self.titulo = Label(self.primeiroContainer, text="Deletar Cliente")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.cpfLabel = Label(self.segundoContainer, text="CPF", font=self.fontePadrao)
        self.cpfLabel.pack(side=LEFT)

        self.cpf = Entry(self.segundoContainer)
        self.cpf["width"] = 30
        self.cpf["font"] = self.fontePadrao
        self.cpf.pack(side=LEFT)

        self.cpfLabel_adm = Label(self.terceiroContainer, text="CPF ADM", font=self.fontePadrao)
        self.cpfLabel_adm.pack(side=LEFT)

        self.cpf_adm = Entry(self.terceiroContainer)
        self.cpf_adm["width"] = 30
        self.cpf_adm["font"] = self.fontePadrao
        self.cpf_adm.pack(side=LEFT)

        self.senhaLabel = Label(self.quartoContainer, text="Senha ADM", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.quartoContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"  # mostrar * quando qualquer caracter for digitado no campo
        self.senha.pack(side=LEFT)

        self.deletar = Button(self.quintoContainer)
        self.deletar["text"] = "Deletar"
        self.deletar["font"] = ("Calibri", "8")
        self.deletar["width"] = 12
        self.deletar["command"] = self.validar_dados
        self.deletar.pack()

        self.mensagem = Label(self.quintoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def validar_dados(self):  # valida os campos, se todos estiverem ok, inserir normalmente no arquivo
        if ControladorSuperADM.login(self.cpf_adm.get(),self.senha.get()):
            if self.cpf.get() == "":
                self.mensagem["text"] = "CPF vazio, por favor informe um CPF"
            else:
                cpf = self.cpf.get()
                resposta = ControladorCliente.deletar_Cliente(cpf)
                if resposta == 'O cpf informado é inválido!':
                    self.mensagem["text"] = resposta
                elif resposta == 'Cliente não encontrado':
                    self.mensagem["text"] = resposta
                elif resposta == 'Deletado com Sucesso':
                    self.mensagem["text"] = resposta
        else:
            self.mensagem["text"] = 'Somente o SuperADM pode deletar dados'