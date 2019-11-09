from Entidades import Funcionario


def funcionario_existe(cpf,linhas):
    posicao = None
    for x in range(0, len(linhas)):
        valores_separados = linhas[x].split(' ')
        if cpf == valores_separados[0]:  # verifica se o cpf é igual ao cpf no arquivo
            posicao = x
    return posicao

def adicionar_Funcionario(funcionario):
    arquivo = open('..\Dados\dbanco\Funcionario.txt', 'r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    posicao = funcionario_existe(funcionario.getCpf(),linhas)
    arquivo.close()
    if posicao is None:#Se o funcionario não existir no arquivo, inserir normalmente
        arquivo = open('..\Dados\dbanco\Funcionario.txt', 'r')
        conteudo = arquivo.readlines()#recebe o conteúdo do arquivo
        conteudo.append(funcionario.getCpf() + ' ' + funcionario.getNome() + ' ' + funcionario.getTelefone() + ' ' + funcionario.getSenha()+'\n')#insere o conteúdo novo
        arquivo = open('..\Dados\dbanco\Funcionario.txt', 'w')
        arquivo.writelines(conteudo)  #escreve no arquivo
        arquivo.close()
        return 'Cadastrado com sucesso'
    else:
        return 'Funcionário já existe'

def limpar_Arquivo():
    arquivo = open('..\Dados\dbanco\Funcionario.txt', 'w')
    arquivo.close()
def deletar_Funcionario(cpf):
    arquivo = open('..\Dados\dbanco\Funcionario.txt','r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    arquivo.close()
    posicao = funcionario_existe(cpf,linhas)
    if posicao is None:
        return 'Funcionário não encontrado'#Não encontrou o Funcionario dentro do arquivo
    else:#Encontrou o Funcionario dentro do arquivo e irá deleta-lo
        linhas.pop(posicao)#Deleta o funcionario encontrado
        arquivo = open('..\Dados\dbanco\Funcionario.txt', 'w')
        arquivo.writelines(linhas)#escreve novamente no arquivo
        arquivo.close()
        return 'Deletado com Sucesso'


def alterar_Funcionario(funcionario):
    arquivo = open('..\Dados\dbanco\Funcionario.txt', 'r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    arquivo.close()
    posicao = funcionario_existe(funcionario.getCpf(),linhas)
    if posicao is None:  # Se o funcionario não existir no arquivo, alteração não funciona
        return "Funcionario não encontrado"
    else:#Se o funcionario existe, alterar normalmente
        arquivo = open('..\Dados\dbanco\Funcionario.txt', 'r')
        conteudo = arquivo.readlines()  # recebe o conteúdo do arquivo
        conteudo[posicao] = funcionario.getCpf() + ' ' + funcionario.getNome() + ' ' + funcionario.getTelefone() + ' ' + funcionario.getSenha() + '\n'#Alterando o funcionario encontrado
        arquivo = open('..\Dados\dbanco\Funcionario.txt', 'w')
        arquivo.writelines(conteudo)#Escrevendo no arquivo
        arquivo.close()
        return 'Funcionario atualizado com sucesso'

def buscar_Funcionario(cpf):
    arquivo = open('..\Dados\dbanco\Funcionario.txt','r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    arquivo.close()
    posicao = funcionario_existe(cpf,linhas)
    if posicao is None:#Se não for encontrado, retornar mensagem de erro
        return 'Usuário não encontrado'
    else:#Caso seja encontrado, retornar um objeto Funcionario
        nome = pegar_nome(linhas[posicao])
        valores = linhas[posicao].split(' ')
        obj = Funcionario.Funcionario(valores[0], nome, valores[len(valores) - 2])#instanciando objeto com cpf, nome e o telefone
        return obj#retornando objeto correspondente a busca

def listar_Funcionarios():
    arquivo = open('..\Dados\dbanco\Funcionario.txt','r')
    linhas = []
    for linha in arquivo:
        linhas.append(linha)
    arquivo.close()
    return linhas
'''
def alterar_senha(cpf,senha_nova):
    arquivo = open('Funcionario.txt','r')
    linhas = []
    for linha in arquivo:  # Percorrer arquivo linha por linha
        linhas.append(linha)  # Adicionar linha numa lista de linhas
    arquivo.close()
    posicao = funcionario_existe(cpf,linhas)
    if posicao is None:
        print('Funcionário não encontrado!')#caso não encontre funcionário, exibir mensagem de erro
    else:
        nome = pegar_nome(linhas[posicao])
        valores = linhas[posicao].split(' ')#se encontrar funcionário, pegar os dados separados dele
        valores[len(valores)-1] = senha_nova#substituindo senha antiga pela nova
        linhas[posicao] = valores[0] + ' ' + nome + ' ' + valores[len(valores)-2] + ' ' + valores[len(valores)-1] + '\n'#substituindo a antiga linha pela nova
        arquivo = open('Funcionario.txt', 'w')
        arquivo.writelines(linhas)#escrevendo no arquivo
        arquivo.close()
'''
def pegar_nome(texto):#Se o nome vier composto, isso é, com espaços, como "joão da silva santos", essa função garante que o nome será retornado normalmente
    texto = texto.split(' ')
    texto.pop(0)#Removendo o primeiro dado(cpf)
    texto.pop(len(texto)-2)#removendo o penultimo dado(telefone)
    texto.pop(len(texto) - 1)#removendo o ultimo dado(senha)
    nome = ''
    for x in texto:
        nome = nome + x + ' '#concatenando os nomes
    nome = nome[:-1]#removendo o espaço em branco que sempre fica no final da string
    return nome

def pegar_senha(cpf):
    arquivo = open('..\Dados\dbanco\Funcionario.txt', 'r')
    linhas = []
    for linha in arquivo:  # Percorrer arquivo linha por linha
        linhas.append(linha)  # Adicionar linha numa lista de linhas
    arquivo.close()
    posicao = funcionario_existe(cpf, linhas)
    if posicao is None:#Se não for encontrado, retornar mensagem de erro
        print('Usuário não encontrado')
    else:#Caso seja encontrado, retornar a senha
        valores = linhas[posicao].split(' ')
        senha = valores[len(valores) - 1]#pegando a senha
        senha = senha[:-1]#removendo o \n
        return senha