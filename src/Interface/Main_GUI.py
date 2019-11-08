from tkinter import *



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

        self.titulo = Label(self.primeiroContainer, text="Bem vindo")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.atualiza_btn = Button(self.segundoContainer)
        self.atualiza_btn["text"] = "Atualizar"
        self.atualiza_btn["font"] = ("Calibri", "8")
        self.atualiza_btn["width"] = 12
        self.atualiza_btn["command"] =
        self.atualiza_btn.pack()


    def atualiza_funcionario(self):
        tela_atualiza = Tk()  # chamando tela de cadastro
        tela_atualiza.geometry('500x500')
        Atualiza_func(tela_atualiza)
        tela_atualiza.mainloop()