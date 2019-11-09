from Dados.repositorios import ClienteRepositorio
from Entidades.Controle import Validation
from Entidades.Cliente import Cliente

def cadastrar_Cliente(cliente):
    if Validation.isCpfValid(cliente.getCpf()):#verifica se o cpf é válido
       resposta = ClienteRepositorio.adicionar_Cliente(cliente)#Insere o cliente
       return resposta
    else:
        return 'CPF invalido, por favor informar um CPF válido'

def deletar_Cliente(cpf):
    if Validation.isCpfValid(cpf):#verifica se o cpf é válido
        resposta = ClienteRepositorio.deletar_Cliente(cpf)#deleta o cliente
        return resposta
    else:
        return 'O cpf informado é inválido!'

def atualizar_Cliente(cliente):
    if Validation.isCpfValid(cliente.getCpf()):#verifica se o cpf é válido
        resposta = ClienteRepositorio.alterar_Cliente(cliente)#altera os dados do cliente
        return resposta
    else:
        return 'O cpf informado é inválido!'

def buscar_Cliente(cpf):
    if Validation.isCpfValid(cpf):#verifica se o cpf é válido
        cliente = ClienteRepositorio.buscar_Cliente(cpf)#recebe o objeto cliente buscado
        return cliente#retorna o objeto
    else:
        return 'O cpf informado é inválido!'

def listar_Clientes():
    texto = ClienteRepositorio.listar_Clientes()#Recebe o texto do arquivo
    lista = []
    for x in range(0,len(texto)):
        splitado = texto[x].split(' ')
        cliente = Cliente(splitado[0], ClienteRepositorio.pegar_nome(texto[x]))
        lista.append(cliente)
    return lista#Retorna uma lista de objetos com cpf e nome