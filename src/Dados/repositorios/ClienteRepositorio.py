from Entidades import Cliente


def cliente_existe(cpf,linhas):
    posicao = None
    for x in range(0, len(linhas)):
        valores_separados = linhas[x].split(' ')
        if cpf == valores_separados[0]:  # verifica se o cpf é igual ao cpf no arquivo
            posicao = x
    return posicao

def adicionar_Cliente(cliente):
    arquivo = open('..\Dados\dbanco\Cliente.txt', 'r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    posicao = cliente_existe(cliente.getCpf(),linhas)
    arquivo.close()
    if posicao is None:#Se o cliente não existir no arquivo, inserir normalmente
        arquivo = open('..\Dados\dbanco\Cliente.txt', 'r')
        conteudo = arquivo.readlines()#recebe o conteúdo do arquivo
        conteudo.append(cliente.getCpf() + ' ' + cliente.getNome() + '\n')#insere o conteúdo novo
        arquivo = open('..\Dados\dbanco\Cliente.txt', 'w')
        arquivo.writelines(conteudo)  #escreve no arquivo
        arquivo.close()
        return 'Cadastrado com sucesso'
    else:
        return 'Cliente já existe'

def limpar_Arquivo():
    arquivo = open('..\Dados\dbanco\Cliente.txt', 'w')
    arquivo.close()

def deletar_Cliente(cpf):
    arquivo = open('..\Dados\dbanco\Cliente.txt','r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    arquivo.close()
    posicao = cliente_existe(cpf,linhas)
    if posicao is None:
        return 'Cliente não encontrado'#Não encontrou o cliente dentro do arquivo
    else:#Encontrou o cliente dentro do arquivo e irá deleta-lo
        linhas.pop(posicao)#Deleta o cliente encontrado
        arquivo = open('..\Dados\dbanco\Cliente.txt', 'w')
        arquivo.writelines(linhas)#escreve novamente no arquivo
        arquivo.close()
        return 'Deletado com Sucesso'

def alterar_Cliente(cliente):
    arquivo = open('..\Dados\dbanco\Cliente.txt', 'r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    arquivo.close()
    posicao = cliente_existe(cliente.getCpf(),linhas)
    if posicao is None:  # Se o cliente não existir no arquivo, alteração não funciona
        return "Cliente não encontrado"
    else:#Se o cliente existe, alterar normalmente
        arquivo = open('..\Dados\dbanco\Cliente.txt', 'r')
        conteudo = arquivo.readlines()  # recebe o conteúdo do arquivo
        conteudo[posicao] = cliente.getCpf() + ' ' + cliente.getNome() + '\n'#Alterando o cliente encontrado
        arquivo = open('..\Dados\dbanco\Cliente.txt', 'w')
        arquivo.writelines(conteudo)#Escrevendo no arquivo
        arquivo.close()
        return 'Cliente atualizado com sucesso'

def buscar_Cliente(cpf):
    arquivo = open('..\Dados\dbanco\Cliente.txt','r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    arquivo.close()
    posicao = cliente_existe(cpf,linhas)
    if posicao is None:#Se não for encontrado, retornar mensagem de erro
        return 'Cliente não encontrado'
    else:#Caso seja encontrado, retornar um objeto Cliente
        nome = pegar_nome(linhas[posicao])
        valores = linhas[posicao].split(' ')
        obj = Cliente.Cliente(valores[0], nome)#instanciando objeto com cpf e nome
        return obj#retornando objeto correspondente a busca

def listar_Clientes():
    arquivo = open('..\Dados\dbanco\Cliente.txt','r')
    linhas = []
    for linha in arquivo:
        linhas.append(linha)
    arquivo.close()
    return linhas

def pegar_nome(texto):#Se o nome vier composto, isso é, com espaços, como "joão da silva santos", essa função garante que o nome será retornado normalmente
    texto = texto.split(' ')
    texto.pop(0)#Removendo o primeiro dado(cpf)
    nome = ''
    for x in texto:
        nome = nome + x + ' '#concatenando os nomes
    nome = nome[:-1]#removendo o \n que sempre fica no final da string
    return nome