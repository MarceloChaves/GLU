from Dados.repositorios import FuncionarioRepositorio
from Entidades.Controle import Validation
from Entidades import Funcionario


def cadastrar_Funcionario(funcionario):
    if Validation.isCpfValid(funcionario.getCpf()):#verifica se o cpf é válido
        if Validation.senhaisValid(funcionario.getSenha()):#verifica se a senha é válida
           resposta = FuncionarioRepositorio.adicionar_Funcionario(funcionario)#Insere o funcionário
           return resposta
        else:
            return 'Senha inválida!'
    else:
        return 'CPF invalido, por favor informar um CPF válido'

def deletar_Funcionario(cpf):
    if Validation.isCpfValid(cpf):#verifica se o cpf é válido
        resposta =FuncionarioRepositorio.deletar_Funcionario(cpf)#deleta o funcionário
        return resposta
    else:
        return 'O cpf informado é inválido!'

def atualizar_Funcionario(funcionario):
    if Validation.isCpfValid(funcionario.getCpf()):#verifica se o cpf é válido
        if Validation.senhaisValid(funcionario.getSenha()):#verifica se a senha é válida
            resposta = FuncionarioRepositorio.alterar_Funcionario(funcionario)#altera os dados do funcionário
            return resposta
        else:
           return 'A senha que você deseja alterar é inválida!'
    else:
        return 'O cpf informado é inválido!'

def buscar_Funcionario(cpf):
    if Validation.isCpfValid(cpf):#verifica se o cpf é válido
        funcionario = FuncionarioRepositorio.buscar_Funcionario(cpf)#recebe o objeto funcionário buscado
        return funcionario#retorna o objeto
    else:
        return 'O cpf informado é inválido!'

def listar_Funcionarios():
    texto = FuncionarioRepositorio.listar_Funcionarios()#Recebe o texto do arquivo
    lista = []
    for x in range(0,len(texto)):
        splitado = texto[x].split(' ')
        funcionario = Funcionario.Funcionario(splitado[0], FuncionarioRepositorio.pegar_nome(texto[x]), splitado[len(splitado) - 2])
        lista.append(funcionario)
    return lista#Retorna uma lista de objetos com cpf,nome e telefone

def login(cpf,senha):
    funcionario = buscar_Funcionario(cpf)
    if funcionario is None:
        return False
    senha_real = FuncionarioRepositorio.pegar_senha(funcionario.getCpf())
    if senha == senha_real:
        return True
    else:
        return False



