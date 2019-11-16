from tkinter import *
from tkinter.ttk import *
from Interface.GUI_Cadastro import Cadastro_func
from Interface.GUI_Funcionario.GUI_Atualiza import Atualiza_func
from Interface.GUI_Funcionario.GUI_Deleta import Deleta_func
from Interface.GUI_Funcionario.GUI_Buscar import Busca_func
from Interface.GUI_Funcionario.GUI_Lista import Lista_func
from Interface.GUI_Cliente.Adiciona_Cliente import Cadastro_cliente
from Interface.GUI_Cliente.Atualiza_Cliente import Atualiza_cliente
from Interface.GUI_Cliente.Deleta_Cliente import Deleta_cliente
from Interface.GUI_Cliente.Buscar_Cliente import Busca_cliente
from Interface.GUI_Cliente.Lista_Cliente import Lista_cliente

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

        botao_cadastro_funcionario = Button(self.frame_aba1,text="Cadastrar", command=self.cadastrar_novo)#Botões para funcionário
        botao_cadastro_funcionario.place( height=30, width=80)
        botao_atualiza_funcionario = Button(self.frame_aba1, text="Alterar", command=self.atualiza_funcionario)
        botao_atualiza_funcionario.place(height=30, width=80, x=0, y=30)
        botao_deleta_funcionario = Button(self.frame_aba1, text="Deletar", command=self.deleta_funcionario)
        botao_deleta_funcionario.place(height=30, width=80, x=0, y=60)
        botao_busca_funcionario = Button(self.frame_aba1, text="Buscar", command=self.busca_funcionario)
        botao_busca_funcionario.place(height=30, width=80, x=0, y=90)
        botao_lista_funcionario = Button(self.frame_aba1, text="listar", command=self.lista_funcionario)
        botao_lista_funcionario.place(height=30, width=80, x=0, y=120)#Botões para Funcionário
        botao_cadastro_produto = Button(self.frame_aba2, text="Cadastrar")
        botao_cadastro_produto.place(height=30, width=80)
        botao_editar_produto = Button(self.frame_aba2, text="Alterar")
        botao_editar_produto.place(height=30, width=80, x=0, y=30)
        botao_nova_venda = Button(self.frame_aba3, text="Nova Venda")
        botao_nova_venda.place(height=30, width=80)
        botao_consulta_produto = Button(self.frame_aba3, text="Ver Preço")
        botao_consulta_produto.place(height=30, width=80, x=0, y=30)
        botao_cadastro_cliente = Button(self.frame_aba4, text="Cadastrar",command=self.adicionar_clientes)#Botões para cliente
        botao_cadastro_cliente.place(height=30, width=80)
        botao_editar_cliente = Button(self.frame_aba4, text="Alterar",command=self.atualiza_cliente)
        botao_editar_cliente.place(height=30, width=80, x=0, y=30)
        botao_deleta_cliente = Button(self.frame_aba4, text="Deletar", command=self.deleta_cliente)
        botao_deleta_cliente.place(height=30, width=80, x=0, y=60)
        botao_busca_cliente = Button(self.frame_aba4, text="Buscar", command=self.busca_cliente)
        botao_busca_cliente.place(height=30, width=80, x=0, y=90)
        botao_lista_cliente = Button(self.frame_aba4, text="Listar", command=self.lista_cliente)
        botao_lista_cliente.place(height=30, width=80, x=0, y=120)#Botões para cliente
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


    def cadastrar_novo(self):
        tela_cadastro = Tk()#chamando tela de cadastro
        Cadastro_func(tela_cadastro)
        tela_cadastro.geometry('500x500')
        tela_cadastro.mainloop()

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

    def adicionar_clientes(self):
        tela_adiciona = Tk()
        tela_adiciona.geometry('500x500')
        Cadastro_cliente(tela_adiciona)
        tela_adiciona.mainloop()

    def atualiza_cliente(self):
        tela_atualiza = Tk()
        tela_atualiza.geometry('500x500')
        Atualiza_cliente(tela_atualiza)
        tela_atualiza.mainloop()

    def deleta_cliente(self):
        tela_deleta = Tk()
        tela_deleta.geometry('500x500')
        Deleta_cliente(tela_deleta)
        tela_deleta.mainloop()

    def busca_cliente(self):
        tela_busca = Tk()
        tela_busca.geometry('500x500')
        Busca_cliente(tela_busca)
        tela_busca.mainloop()

    def lista_cliente(self):
        tela_lista = Tk()
        tela_lista.geometry('500x500')
        Lista_cliente(tela_lista)
        tela_lista.mainloop()