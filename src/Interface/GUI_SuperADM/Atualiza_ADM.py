from tkinter import *
from Entidades.Controle import ControladorSuperADM
from Entidades.SuperADM import SuperADM


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


class Atualiza_adm:
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

        self.setimoContainer = Frame(master)
        self.setimoContainer["pady"] = 20
        self.setimoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Atualizar Adm")
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

        self.senhaLabel_atual = Label(self.sextoContainer, text="Senha Atual", font=self.fontePadrao)
        self.senhaLabel_atual.pack(side=LEFT)

        self.senha_atual = Entry(self.sextoContainer)
        self.senha_atual["width"] = 30
        self.senha_atual["font"] = self.fontePadrao
        self.senha_atual["show"] = "*"
        self.senha_atual.pack(side=LEFT)

        self.criar = Button(self.setimoContainer)
        self.criar["text"] = "Alterar"
        self.criar["font"] = ("Calibri", "8")
        self.criar["width"] = 12
        self.criar["command"] = self.validar_dados
        self.criar.pack()

    def validar_dados(self):  # valida os campos, se todos estiverem ok, atualizar normalmente no arquivo
        if ControladorSuperADM.login(self.cpf.get(),self.senha_atual.get()):
            if self.cpf.get() == "": #verificando se todos os campos estão preenchidos
                popup_erro("CPF vazio, por favor informe um CPF")
            elif self.senha.get() == "":
                popup_erro("Senha vazia, por favor informe uma Senha")
            elif self.nome.get() == "":
                popup_erro("Nome vazio, por favor informe um Nome")
            elif self.telefone.get() == "":
                popup_erro("Telefone vazio, por favor informe um Telefone")
            else:  #se todos estiverem preenchidos, valida-los
                splited = self.telefone.get().split(' ')  #removendo os espaços em branco no telefone
                telefone = ''
                for x in splited:
                    telefone = telefone + x
                senha = self.senha.get()
                nome = self.nome.get()
                cpf = self.cpf.get()
                adm = SuperADM(cpf, nome, telefone)#instanciando objeto com os dados
                adm.setSenha(senha) #setando a senha
                resposta = ControladorSuperADM.atualizar_Adm(adm)#chamando a função para atualizar no arquivo
                if resposta == 'O cpf informado é inválido!':
                    popup_erro(resposta)
                elif resposta == 'A senha que você deseja alterar é inválida!':
                    popup_erro(resposta)
                elif resposta == "ADM não encontrado":
                    popup_erro(resposta)
                elif resposta == 'ADM atualizado com sucesso': #se não houver nenhum problema, avisar ao usuário que a operação ocorreu com sucesso
                    popup_sucesso(resposta)
        else:
            popup_erro('Somente o ADM pode atualizar seus dados')