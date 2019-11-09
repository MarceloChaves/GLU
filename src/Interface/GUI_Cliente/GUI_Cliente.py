from tkinter import *
from Interface.GUI_Cliente.Adiciona_Cliente import Cadastro_cliente
from Interface.GUI_Cliente.Lista_Cliente import Lista_cliente
from Interface.GUI_Cliente.Buscar_Cliente import Busca_cliente
from Interface.GUI_Cliente.Deleta_Cliente import Deleta_cliente
from Interface.GUI_Cliente.Atualiza_Cliente import Atualiza_cliente

class Crud_Cliente:
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

        self.titulo = Label(self.primeiroContainer, text="Gerenciar Clientes")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.atualiza_btn = Button(self.segundoContainer)
        self.atualiza_btn["text"] = "Atualizar"
        self.atualiza_btn["font"] = ("Calibri", "8")
        self.atualiza_btn["width"] = 12
        self.atualiza_btn["command"] = self.atualiza_cliente
        self.atualiza_btn.pack()

        self.deleta_btn = Button(self.terceiroContainer)
        self.deleta_btn["text"] = "Deletar"
        self.deleta_btn["font"] = ("Calibri", "8")
        self.deleta_btn["width"] = 12
        self.deleta_btn["command"] = self.deleta_cliente
        self.deleta_btn.pack()

        self.busca_btn = Button(self.quartoContainer)
        self.busca_btn["text"] = "Buscar"
        self.busca_btn["font"] = ("Calibri", "8")
        self.busca_btn["width"] = 12
        self.busca_btn["command"] = self.busca_cliente
        self.busca_btn.pack()

        self.lisar_btn = Button(self.quintoContainer)
        self.lisar_btn["text"] = "Listar"
        self.lisar_btn["font"] = ("Calibri", "8")
        self.lisar_btn["width"] = 12
        self.lisar_btn["command"] = self.lista_cliente
        self.lisar_btn.pack()

        self.adicionar_btn = Button(self.sextoContainer)
        self.adicionar_btn["text"] = "Cadastrar"
        self.adicionar_btn["font"] = ("Calibri", "8")
        self.adicionar_btn["width"] = 12
        self.adicionar_btn["command"] = self.adicionar_clientes
        self.adicionar_btn.pack()

    def adicionar_clientes(self):
        tela_adiciona = Tk()
        tela_adiciona.geometry('500x500')
        Cadastro_cliente(tela_adiciona)
        tela_adiciona.mainloop()

    def lista_cliente(self):
        tela_lista = Tk()
        tela_lista.geometry('500x500')
        Lista_cliente(tela_lista)
        tela_lista.mainloop()

    def busca_cliente(self):
        tela_busca = Tk()
        tela_busca.geometry('500x500')
        Busca_cliente(tela_busca)
        tela_busca.mainloop()

    def deleta_cliente(self):
        tela_deleta = Tk()
        tela_deleta.geometry('500x500')
        Deleta_cliente(tela_deleta)
        tela_deleta.mainloop()

    def atualiza_cliente(self):
        tela_atualiza = Tk()
        tela_atualiza.geometry('500x500')
        Atualiza_cliente(tela_atualiza)
        tela_atualiza.mainloop()