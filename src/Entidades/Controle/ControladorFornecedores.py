from Dados.repositorios import FornecedoresRepositorio
from Entidades.Controle import Validation
from Entidades import Fornecedores


def cadastrar_Fornecedor(fornecedor):
    if Validation.isCpfValid(Fornecedores.getCnpj()):#verifica se o cnpj é válido
        if Validation.senhaisValid(Fornecedores.getSenha()):#verifica se a senha é válida
           resposta = FornecedoresRepositorio.adicionar_Fornecedores(fornecedor)#Insere o fonecedor
           return resposta
        else:
            return 'Senha inválida!'
    else:
        return 'CNPJ invalido, por favor informar um CNPJ válido'

def deletar_Fornecedor(cnpj):
    if Validation.isCnpjValid(cnpj):#verifica se o cnpj é válido
        resposta =FornecedoresRepositorio.deletar_Fornecedor(cnpj)#deleta o fornecedor
        return resposta
    else:
        return 'O cnpj informado é inválido!'

def atualizar_Fornecedor(fornecedores):
    if Validation.isCnpjValid(fornecedores.getCnpj()):#verifica se o cnpj é válido
        if Validation.senhaisValid(fornecedores.getSenha()):#verifica se a senha é válida
            resposta = FornecedoresRepositorio.alterar_Fornecedores(fornecedores)#altera os dados do fornecedores
            return resposta
        else:
           return 'A senha que você deseja alterar é inválida!'
    else:
        return 'O cnpj informado é inválido!'

def buscar_Fornecedor(cnpj):
    if Validation.isCnpjValid(cnpj):#verifica se o cnpj é válido
        fornecedores = FornecedoresRepositorio.buscar_Fornecedores(cnpj)#recebe o objeto fornecedores buscado
        return fornecedores#retorna o objeto
    else:
        return 'O cnpj informado é inválido!'

def listar_Fornecedores():
    texto = FornecedoresRepositorio.listar_Fornecedores()#Recebe o texto do arquivo
    lista = []
    for x in range(0,len(texto)):
        splitado = texto[x].split(' ')
        fornecedor = Fornecedores.Funcionario(splitado[0], FornecedoresRepositorio.pegar_nome(texto[x]), splitado[len(splitado) - 2])
        lista.append(fornecedor)
    return lista#Retorna uma lista de objetos com cnpj,nome e telefone

def login(cnpj,senha):
    fornecedores = buscar_Fornecedor(cnpj)
    if isinstance(fornecedores,str):
        return False
    senha_real = FornecedoresRepositorio.pegar_senha(fornecedores.getCnpj())
    if senha == senha_real:
        return True
    else:
        return False