from tkinter import *
from Entidades.Controle import ControladorCliente
from Entidades.Cliente import Cliente


def popup_erro(mensagem):
    popup = Tk()
    popup.wm_title('Erro')
    label = Label(popup, text=mensagem)
    label.pack(side='top', fill='x', pady=10)
    b1 = Button(popup, text="Entendi", command=popup.destroy)
    b1.pack()
    popup.mainloop()


def popup_sucesso(mensagem):
    popup = Tk()
    popup.wm_title('Sucesso!')
    label = Label(popup, text=mensagem)
    label.pack(side='top', fill='x', pady=10)
    b1 = Button(popup, text="OK", command=popup.destroy)
    b1.pack()
    popup.mainloop()


class Atualiza_cliente:
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

        self.titulo = Label(self.primeiroContainer, text="Atualizar Cliente")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.cpfLabel = Label(self.segundoContainer, text="CPF", font=self.fontePadrao)
        self.cpfLabel.pack(side=LEFT)

        self.cpf = Entry(self.segundoContainer)
        self.cpf["width"] = 30
        self.cpf["font"] = self.fontePadrao
        self.cpf.pack(side=LEFT)

        self.nomeLabel = Label(self.terceiroContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.terceiroContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.criar = Button(self.quartoContainer)
        self.criar["text"] = "Atualizar"
        self.criar["font"] = ("Calibri", "8")
        self.criar["width"] = 12
        self.criar["command"] = self.validar_dados
        self.criar.pack()

    def validar_dados(self):  # valida os campos, se todos estiverem ok, inserir normalmente no arquivo
        if self.cpf.get() == "":
            popup_erro("CPF vazio, por favor informe um CPF")
        elif self.nome.get() == "":
            popup_erro("Nome vazio, por favor informe um Nome")
        else:
            nome = self.nome.get()
            cpf = self.cpf.get()
            cliente = Cliente(cpf, nome)
            resposta = ControladorCliente.atualizar_Cliente(cliente)
            if resposta == 'O cpf informado é inválido!':
                popup_erro(resposta)
            elif resposta == "Cliente não encontrado":
                popup_erro(resposta)
            elif resposta == 'Cliente atualizado com sucesso':
                popup_sucesso(resposta)
