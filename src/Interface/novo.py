from Interface.Teste import Main
from tkinter import *
'''
root = Tk()
root.configure(background='blue')
root.title("Gerenciamento de Loja Universal - GLU")
root.geometry("720x350")
Main(root)
root.mainloop()
'''
def abremain():
    root = Tk()
    root.configure(background='blue')
    root.title("Gerenciamento de Loja Universal - GLU")
    root.geometry("720x350")
    Main(root)
    root.mainloop()


class Novo:
    def __init__(self,master=None):
        self.master = master
        self.fontePadrao = ("Arial", "10")  # definindo a fonte
        self.primeiroContainer = Frame(self.master)  # Criando containers
        self.primeiroContainer.pack()

        self.autenticar = Button(self.primeiroContainer)  # botão para logar
        self.autenticar["text"] = "Entrar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.abremain
        self.autenticar.pack()

    def abremain(self):
        abremain()




raiz = Tk()
Novo(raiz)
raiz.mainloop()
abremain()