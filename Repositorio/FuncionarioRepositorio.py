from Controle import Funcionario

def Adicionar_Funcionario(funcionario):
    arquivo = open('Funcionario.txt', 'r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    posicao = None
    for x in range(0, len(linhas)):
        if funcionario.getCpf() in linhas[x]:#Se a busca encontrar o cpf na linha, pegamos a posição na lista de linhas
            posicao = x
    arquivo.close()
    if posicao is None:#Se o funcionario não existir no arquivo, inserir normalmente
        arquivo = open('Funcionario.txt', 'r')
        conteudo = arquivo.readlines()#recebe o conteúdo do arquivo
        conteudo.append(funcionario.getCpf() + ' ' + funcionario.getNome() + ' ' + funcionario.getTelefone() + '\n')#insere o conteúdo novo
        arquivo = open('Funcionario.txt', 'w')
        arquivo.writelines(conteudo)  #escreve no arquivo
    else:
        print('Funcionário já existe')
    arquivo.close()
def Limpar_arquivo():
    arquivo = open('Funcionario.txt', 'w')
    arquivo.close()
def Deletar_funcionario(cpf):
    arquivo = open('Funcionario.txt','r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    posicao = None
    for x in range(0,len(linhas)):
        if cpf in linhas[x]:
            posicao = x
    if posicao is None:
        print('Funcionário não encontrado')#Não encontrou o Funcionario dentro do arquivo
    else:#Encontrou o Funcionario dentro do arquivo e irá deleta-lo
        linhas.pop(posicao)#Deleta o funcionario encontrado
        arquivo = open('Funcionario.txt', 'w')
        arquivo.writelines(linhas)#escreve novamente no arquivo

    arquivo.close()
def Alterar_Funcionario(funcionario):
    arquivo = open('Funcionario.txt', 'r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    posicao = None
    for x in range(0, len(linhas)):
        if funcionario.getCpf() in linhas[x]:#Se a busca encontrar o cpf na linha, pegamos a posição na lista de linhas
            posicao = x
    arquivo.close()
    if posicao is None:  # Se o funcionario não existir no arquivo, alteração não funciona
        print("Funcionario não encontrado")
    else:#Se o funcionario existe, alterar normalmente
        arquivo = open('Funcionario.txt', 'r')
        conteudo = arquivo.readlines()  # recebe o conteúdo do arquivo
        conteudo[posicao] = funcionario.getCpf() + ' ' + funcionario.getNome() + ' ' + funcionario.getTelefone() + '\n'#Alterando o funcionario encontrado
        arquivo = open('Funcionario.txt', 'w')
        arquivo.writelines(conteudo)#Escrevendo no arquivo
    arquivo.close()
def Buscar_Funcionario(cpf):
    arquivo = open('Funcionario.txt','r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    posicao = None
    for x in range(0, len(linhas)):
        if cpf in linhas[x]:#Se a busca encontrar o cpf na linha, pegamos a posição na lista de linhas
            posicao = x
    arquivo.close()
    if posicao is None:#Se não for encontrado, retornar mensagem de erro
        print('Usuário não encontrado')
    else:#Caso seja encontrado, retornar um objeto Funcionario
        valores = linhas[posicao].split(' ')
        obj = Funcionario.Funcionario(valores[0],valores[1],valores[2])
        return obj

def Listar_Funcionarios():
    arquivo = open('Funcionario.txt','r')
    linhas = []
    for linha in arquivo:
        linhas.append(linha)
    print(linhas)
    arquivo.close()

Listar_Funcionarios()


