from tkinter import *
from Entidades.Controle import ControladorFuncionario
from Interface.GUI_Cadastro import Cadastro_func
from Interface.Main_GUI import Tela_Principal

def popup_erro(mensagem):
    popup = Tk()
    popup.wm_title('Erro')
    label = Label(popup,text = mensagem)
    label.pack(side='top', fill='x', pady=10)
    b1 = Button(popup,text="Entendi", command = popup.destroy)
    b1.pack()
    popup.mainloop()



class Application:
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
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Login Funcionário")
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
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Entrar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.abrir_cadastro = Button(self.quintoContainer)
        self.abrir_cadastro["text"] = "Cadastrar"
        self.abrir_cadastro["font"] = ("Calibri", "8")
        self.abrir_cadastro["width"] = 12
        self.abrir_cadastro["command"] = self.cadastrar_novo
        self.abrir_cadastro.pack()

        self.mensagem2 = Label(self.quintoContainer, text="", font=self.fontePadrao)
        self.mensagem2.pack()


    # Método verificar senha
    def verificaSenha(self):
        cpf = self.cpf.get()
        senha = self.senha.get()
        if ControladorFuncionario.login(cpf,senha):
            funcionario = ControladorFuncionario.buscar_Funcionario(cpf)
            tela_principal = Tk()
            Tela_Principal(tela_principal)
            tela_principal.mainloop()
        else:
            popup_erro("senha ou cpf incorretos")
    #chamando tela de cadastro
    def cadastrar_novo(self):
        tela_cadastro = Tk()#chamando tela de cadastro
        Cadastro_func(tela_cadastro)
        tela_cadastro.geometry('500x500')
        tela_cadastro.mainloop()


root = Tk()
Application(root)
root.mainloop()