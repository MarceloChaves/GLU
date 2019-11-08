from tkinter import *
from Entidades.Controle import ControladorFuncionario

class Lista_func:
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

        self.titulo = Label(self.primeiroContainer, text="Listar Funcionário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.listar = Button(self.segundoContainer)
        self.listar["text"] = "Listar"
        self.listar["font"] = ("Calibri", "8")
        self.listar["width"] = 12
        self.listar["command"] = self.validar_dados
        self.listar.pack()

        self.mensagem = Label(self.segundoContainer, text="CPF     Nome      Telefone", font=self.fontePadrao)
        self.mensagem.pack()


    def validar_dados(self):  # valida os campos, se todos estiverem ok, inserir normalmente no arquivo
        lista = ControladorFuncionario.listar_Funcionarios()
        self.height = len(lista)
        self.width = 3
        celulas = {}
        for i in range(self.height):  # linha
            for j in range(self.width):  # Coluna
                campo = Entry(self.terceiroContainer, text="")
                campo.grid(row=i, column=j)
                celulas[(i, j)] = campo
        for i in range(self.height):  # linha
            for j in range(self.width):  # Coluna
                if j==0:
                    celulas[(i,j)].insert(0,lista[i].getCpf())
                elif j==1:
                    celulas[(i, j)].insert(0, lista[i].getNome())
                elif j==2:
                    celulas[(i, j)].insert(0, lista[i].getTelefone())