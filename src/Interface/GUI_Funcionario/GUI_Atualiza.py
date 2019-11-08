from tkinter import *
from Entidades.Controle import ControladorFuncionario
from Entidades import Funcionario


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


class Atualiza_func:
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

        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 20
        self.sextoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Atualizar Funcionário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.cpfLabel = Label(self.segundoContainer, text="CPF", font=self.fontePadrao)
        self.cpfLabel.pack(side=LEFT)

        self.cpf = Entry(self.segundoContainer)
        self.cpf["width"] = 30
        self.cpf["font"] = self.fontePadrao
        self.cpf.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha.pack(side=LEFT)

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

        self.criar = Button(self.sextoContainer)
        self.criar["text"] = "Entrar"
        self.criar["font"] = ("Calibri", "8")
        self.criar["width"] = 12
        self.criar["command"] = self.validar_dados
        self.criar.pack()

    def validar_dados(self):  # valida os campos, se todos estiverem ok, inserir normalmente no arquivo
        if self.cpf.get() == "":
            popup_erro("CPF vazio, por favor informe um CPF")
        elif self.senha.get() == "":
            popup_erro("Senha vazia, por favor informe uma Senha")
        elif self.nome.get() == "":
            popup_erro("Nome vazio, por favor informe um Nome")
        elif self.telefone.get() == "":
            popup_erro("Telefone vazio, por favor informe um Telefone")
        else:
            splited = self.telefone.get().split(' ')
            telefone = ''
            for x in splited:
                telefone = telefone + x
            senha = self.senha.get()
            nome = self.nome.get()
            cpf = self.cpf.get()
            funcionario = Funcionario.Funcionario(cpf, nome, telefone)
            funcionario.setSenha(senha)
            resposta = ControladorFuncionario.atualizar_Funcionario(funcionario)
            if resposta == 'CPF invalido, por favor informar um CPF válido':
                popup_erro(resposta)
            elif resposta == 'Senha inválida!':
                popup_erro(resposta)
            elif resposta == 'Funcionário já existe':
                popup_erro(resposta)
            elif resposta == 'Cadastrado com sucesso':
                popup_sucesso(resposta)
