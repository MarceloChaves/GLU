from Dados.repositorios import SuperADMRepositorio
from Entidades.Controle import Validation
from Entidades import SuperADM


def cadastrar_Adm(adm):
    if Validation.isCpfValid(adm.getCpf()):#verifica se o cpf é válido
        if Validation.senhaisValid(adm.getSenha()):#verifica se a senha é válida
           resposta = SuperADMRepositorio.adicionar_Adm(adm)#Insere o ADM
           return resposta
        else:
            return 'Senha inválida!'
    else:
        return 'CPF invalido, por favor informar um CPF válido'

def deletar_Adm(cpf):
    if Validation.isCpfValid(cpf):#verifica se o cpf é válido
        resposta =SuperADMRepositorio.deletar_Adm(cpf)#deleta o ADM
        return resposta
    else:
        return 'O cpf informado é inválido!'

def atualizar_Adm(adm):
    if Validation.isCpfValid(adm.getCpf()):#verifica se o cpf é válido
        if Validation.senhaisValid(adm.getSenha()):#verifica se a senha é válida
            resposta = SuperADMRepositorio.alterar_Adm(adm)#altera os dados do adm
            return resposta
        else:
           return 'A senha que você deseja alterar é inválida!'
    else:
        return 'O cpf informado é inválido!'

def buscar_Adm(cpf):
    if Validation.isCpfValid(cpf):#verifica se o cpf é válido
        adm = SuperADMRepositorio.buscar_Adm(cpf)#recebe o objeto ADM buscado
        return adm#retorna o objeto
    else:
        return 'O cpf informado é inválido!'

def listar_Adm():
    texto = SuperADMRepositorio.listar_Adm()#Recebe o texto do arquivo
    lista = []
    for x in range(0,len(texto)):
        splitado = texto[x].split(' ')
        adm = SuperADM.SuperADM(splitado[0], SuperADMRepositorio.pegar_nome(texto[x]), splitado[len(splitado) - 2])
        lista.append(adm)
    return lista#Retorna uma lista de objetos com cpf,nome e telefone

def login(cpf,senha):
    adm = buscar_Adm(cpf)
    if isinstance(adm,str):
        return False
    senha_real = SuperADMRepositorio.pegar_senha(adm.getCpf())
    if senha == senha_real:
        return True
    else:
        return False



