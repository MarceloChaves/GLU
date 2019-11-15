from tkinter import *
from tkinter.ttk import *
import tkinter as tk
#root = tk.Tk()
#root.configure(background='blue')
#root.title("Gerenciamento de Loja Universal - GLU")
#root.geometry("720x350")
class Main:
    def __init__(self,master):
        self.root = master
        self.abas = Notebook(self.root)
        self.frame_aba1 = Frame(self.abas)
        self.frame_aba2 = Frame(self.abas)
        self.frame_aba3 = Frame(self.abas)
        self.frame_aba4 = Frame(self.abas)
        self.abas.add(self.frame_aba1,text="Cadastro de Funcionario")
        self.abas.add(self.frame_aba2,text="Estoque")
        self.abas.add(self.frame_aba3,text="Vendas")
        self.abas.add(self.frame_aba4,text="Cadastro Cliente")
        self.abas.pack(fill = BOTH)

        botao_cadastro_funcionario = Button(self.frame_aba1,text="Cadastrar")
        botao_cadastro_funcionario.place( height=30, width=80)
        botao_editar_funcionario = Button(self.frame_aba1, text="Alterar")
        botao_editar_funcionario.place(height=30, width=80 , x=0 , y=30)
        botao_cadastro_produto = Button(self.frame_aba2, text="Cadastrar")
        botao_cadastro_produto.place(height=30, width=80)
        botao_editar_produto = Button(self.frame_aba2, text="Alterar")
        botao_editar_produto.place(height=30, width=80, x=0, y=30)
        botao_nova_venda = Button(self.frame_aba3, text="Nova Venda")
        botao_nova_venda.place(height=30, width=80)
        botao_consulta_produto = Button(self.frame_aba3, text="Ver Preço")
        botao_consulta_produto.place(height=30, width=80, x=0, y=30)
        botao_cadastro_cliente = Button(self.frame_aba4, text="Cadastrar")
        botao_cadastro_cliente.place(height=30, width=80)
        botao_editar_cliente = Button(self.frame_aba4, text="Alterar")
        botao_editar_cliente.place(height=30, width=80, x=0, y=30)
        botao_editar_funcionario = Button(self.frame_aba1, text="Alterar")
        botao_editar_funcionario.place(height=30, width=80, x=0, y=30)
        botao_editar_funcionario = Button(self.frame_aba1, text="Alterar")
        botao_editar_funcionario.place(height=30, width=80, x=0, y=30)
        botao_sair= Button(self.root,text="Sair",command=self.root.destroy)
        botao_sair.pack(padx=5,pady=5)

        imagem1 = PhotoImage(file="funcionario.png")
        imagem2 = PhotoImage(file="estoque.png")
        imagem3 = PhotoImage(file="carrinho.png")
        imagem4 = PhotoImage(file="cliente.png")
        w1 = Label(self.frame_aba1, image=imagem1, compound=CENTER)
        w2 = Label(self.frame_aba2, image=imagem2, compound=CENTER)
        w3 = Label(self.frame_aba3, image=imagem3, compound=CENTER)
        w4 = Label(self.frame_aba4, image=imagem4, compound=CENTER)
        w1.imagem = imagem1
        w2.imagem = imagem2
        w3.imagem = imagem3
        w4.imagem = imagem4
        w1.pack(side = RIGHT)
        w2.pack(side = RIGHT)
        w3.pack(side = RIGHT)
        w4.pack(side = RIGHT)



#Main(root)
#root.mainloop()