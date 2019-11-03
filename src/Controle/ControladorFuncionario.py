from src.Repositorio import FuncionarioRepositorio
from src.Controle import Validation, Funcionario


def cadastrar_Funcionario(funcionario):
    if Validation.isCpfValid(funcionario.getCpf()):
        FuncionarioRepositorio.adicionar_Funcionario(funcionario)
    else:
        print('CPF invalido, por favor informar um CPF válido')
