from tkinter import *
from Interface.GUI_Funcionario.GUI_Atualiza import Atualiza_func
from Interface.GUI_Funcionario.GUI_Deleta import Deleta_func
from Interface.GUI_Funcionario.GUI_Lista import Lista_func
from Interface.GUI_Funcionario.GUI_Buscar import Busca_func
from Interface.GUI_Cliente.GUI_Cliente import Crud_Cliente




class Tela_Principal:
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

        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 20
        self.sextoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Bem vindo")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.atualiza_btn = Button(self.segundoContainer)
        self.atualiza_btn["text"] = "Atualizar"
        self.atualiza_btn["font"] = ("Calibri", "8")
        self.atualiza_btn["width"] = 12
        self.atualiza_btn["command"] = self.atualiza_funcionario
        self.atualiza_btn.pack()

        self.deleta_btn = Button(self.terceiroContainer)
        self.deleta_btn["text"] = "Deletar"
        self.deleta_btn["font"] = ("Calibri", "8")
        self.deleta_btn["width"] = 12
        self.deleta_btn["command"] = self.deleta_funcionario
        self.deleta_btn.pack()

        self.busca_btn = Button(self.quartoContainer)
        self.busca_btn["text"] = "Buscar"
        self.busca_btn["font"] = ("Calibri", "8")
        self.busca_btn["width"] = 12
        self.busca_btn["command"] = self.busca_funcionario
        self.busca_btn.pack()

        self.lisar_btn = Button(self.quintoContainer)
        self.lisar_btn["text"] = "Listar"
        self.lisar_btn["font"] = ("Calibri", "8")
        self.lisar_btn["width"] = 12
        self.lisar_btn["command"] = self.lista_funcionario
        self.lisar_btn.pack()

        self.clientes_btn = Button(self.sextoContainer)
        self.clientes_btn["text"] = "Clientes"
        self.clientes_btn["font"] = ("Calibri", "8")
        self.clientes_btn["width"] = 12
        self.clientes_btn["command"] = self.gerenciar_clientes
        self.clientes_btn.pack()

    def atualiza_funcionario(self):
        tela_atualiza = Tk()  # chamando tela de atualização
        tela_atualiza.geometry('500x500')
        Atualiza_func(tela_atualiza)
        tela_atualiza.mainloop()

    def deleta_funcionario(self):
        tela_deleta = Tk()  # chamando tela de exclusão
        tela_deleta.geometry('500x500')
        Deleta_func(tela_deleta)
        tela_deleta.mainloop()

    def busca_funcionario(self):
        tela_busca = Tk()  # chamando tela de busca
        tela_busca.geometry('500x500')
        Busca_func(tela_busca)
        tela_busca.mainloop()

    def lista_funcionario(self):
        tela_lista = Tk()  # chamando tela de listagem
        tela_lista.geometry('500x500')
        Lista_func(tela_lista)
        tela_lista.mainloop()

    def gerenciar_clientes(self):
        tela_cliente = Tk()#chamando tela para gerenciamento de clientes
        tela_cliente.geometry('500x500')
        Crud_Cliente(tela_cliente)
        tela_cliente.mainloop()