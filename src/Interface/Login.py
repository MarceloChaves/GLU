from tkinter import *
from Entidades.Controle import ControladorFuncionario
from Interface.GUI_Cadastro import Cadastro_func
from Interface.Principal import Main
from Entidades.Controle import ControladorSuperADM

def popup_erro(mensagem):
    popup = Tk()
    popup.wm_title('Erro')
    label = Label(popup,text = mensagem)#Recebe a mensagem do erro reportado
    label.pack(side='top', fill='x', pady=10)
    b1 = Button(popup,text="Entendi", command = popup.destroy)#Botão que fecha a janela ao ser clicado
    b1.pack()
    popup.mainloop()

def abremain():
    root = Tk()
    root.configure(background='blue')
    root.title("Gerenciamento de Loja Universal - GLU")
    root.geometry("720x350")
    Main(root)
    root.mainloop()



class Application:
    def __init__(self, master=None):
        self.master = master
        self.fontePadrao = ("Arial", "10")#definindo a fonte
        self.primeiroContainer = Frame(master)#Criando containers
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

        self.titulo = Label(self.primeiroContainer, text="Login Funcionário")#definindo o título
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.cpfLabel = Label(self.segundoContainer, text="CPF", font=self.fontePadrao)#label do cpf
        self.cpfLabel.pack(side=LEFT)

        self.cpf = Entry(self.segundoContainer)#input do cpf
        self.cpf["width"] = 30
        self.cpf["font"] = self.fontePadrao
        self.cpf.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"#mostrar * quando qualquer caracter for digitado no campo
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)#botão para logar
        self.autenticar["text"] = "Entrar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.abrir_cadastro = Button(self.quintoContainer)#botão para cadastrar um novo funcionário
        self.abrir_cadastro["text"] = "Cadastrar"
        self.abrir_cadastro["font"] = ("Calibri", "8")
        self.abrir_cadastro["width"] = 12
        self.abrir_cadastro["command"] = self.cadastrar_novo
        self.abrir_cadastro.pack()


    # Método verificar senha
    def verificaSenha(self):
        cpf = self.cpf.get()
        senha = self.senha.get()
        if ControladorFuncionario.login(cpf,senha) or ControladorSuperADM.login(cpf,senha):#verifica se o cpf e senha batem
            global passou
            passou = True
            self.master.destroy()
        else:
            popup_erro("senha ou cpf incorretos")#exibir popup de erro com mensagem informando que o login falhou
    #chamando tela de cadastro
    def cadastrar_novo(self):
        tela_cadastro = Tk()#chamando tela de cadastro
        Cadastro_func(tela_cadastro)
        tela_cadastro.geometry('500x500')
        tela_cadastro.mainloop()
passou = False
root = Tk()
Application(root)
root.mainloop()
if passou:
    abremain()