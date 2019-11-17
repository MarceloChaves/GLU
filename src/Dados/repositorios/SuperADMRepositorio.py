from Entidades import SuperADM


def adm_existe(cpf,linhas):
    posicao = None
    for x in range(0, len(linhas)):
        valores_separados = linhas[x].split(' ')
        if cpf == valores_separados[0]:  # verifica se o cpf é igual ao cpf no arquivo
            posicao = x
    return posicao

def adicionar_Adm(adm):
    arquivo2 = open('..\Dados\dbanco\Funcionario.txt', 'r')
    linhas = []
    for linha in arquivo2:  # Percorrer arquivo linha por linha
        linhas.append(linha)  # Adicionar linha numa lista de linhas
    posicao_func = adm_existe(adm.getCpf(), linhas)
    arquivo2.close()
    if posicao_func is None:#verifica se o cpf existe em funcionarios
        arquivo = open('..\Dados\dbanco\SuperADM.txt', 'r')
        linhas = []
        for linha in arquivo:#Percorrer arquivo linha por linha
            linhas.append(linha)#Adicionar linha numa lista de linhas
        posicao = adm_existe(adm.getCpf(),linhas)
        arquivo.close()
        if posicao is None:#Se o ADM não existir no arquivo, inserir normalmente
            arquivo = open('..\Dados\dbanco\SuperADM.txt', 'r')
            conteudo = arquivo.readlines()#recebe o conteúdo do arquivo
            conteudo.append(adm.getCpf() + ' ' + adm.getNome() + ' ' + adm.getTelefone() + ' ' + adm.getSenha()+'\n')#insere o conteúdo novo
            arquivo = open('..\Dados\dbanco\SuperADM.txt', 'w')
            arquivo.writelines(conteudo)  #escreve no arquivo
            arquivo.close()
            return 'Cadastrado com sucesso'
        else:
            return 'ADM já existe'
    else:
        return 'Um SuperADM não pode ter o mesmo cpf que um funcionario'
def limpar_Arquivo():
    arquivo = open('..\Dados\dbanco\SuperADM.txt', 'w')
    arquivo.close()
def deletar_Adm(cpf):
    arquivo = open('..\Dados\dbanco\SuperADM.txt','r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    arquivo.close()
    posicao = adm_existe(cpf,linhas)
    if posicao is None:
        return 'ADM não encontrado'#Não encontrou o adm dentro do arquivo
    else:#Encontrou o adm dentro do arquivo e irá deleta-lo
        linhas.pop(posicao)#Deleta o adm encontrado
        arquivo = open('..\Dados\dbanco\SuperADM.txt', 'w')
        arquivo.writelines(linhas)#escreve novamente no arquivo
        arquivo.close()
        return 'Deletado com Sucesso'


def alterar_Adm(adm):
    arquivo = open('..\Dados\dbanco\SuperADM.txt', 'r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    arquivo.close()
    posicao = adm_existe(adm.getCpf(),linhas)
    if posicao is None:  # Se o adm não existir no arquivo, alteração não funciona
        return "ADM não encontrado"
    else:#Se o adm existe, alterar normalmente
        arquivo = open('..\Dados\dbanco\SuperADM.txt', 'r')
        conteudo = arquivo.readlines()  # recebe o conteúdo do arquivo
        conteudo[posicao] = adm.getCpf() + ' ' + adm.getNome() + ' ' + adm.getTelefone() + ' ' + adm.getSenha() + '\n'#Alterando o adm encontrado
        arquivo = open('..\Dados\dbanco\SuperADM.txt', 'w')
        arquivo.writelines(conteudo)#Escrevendo no arquivo
        arquivo.close()
        return 'ADM atualizado com sucesso'

def buscar_Adm(cpf):
    arquivo = open('..\Dados\dbanco\SuperADM.txt','r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    arquivo.close()
    posicao = adm_existe(cpf,linhas)
    if posicao is None:#Se não for encontrado, retornar mensagem de erro
        return 'Usuário não encontrado'
    else:#Caso seja encontrado, retornar um objeto ADM
        nome = pegar_nome(linhas[posicao])
        valores = linhas[posicao].split(' ')
        obj = SuperADM.SuperADM(valores[0], nome, valores[len(valores) - 2])#instanciando objeto com cpf, nome e o telefone
        return obj#retornando objeto correspondente a busca

def listar_Adm():
    arquivo = open('..\Dados\dbanco\SuperADM.txt','r')
    linhas = []
    for linha in arquivo:
        linhas.append(linha)
    arquivo.close()
    return linhas

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
    arquivo = open('..\Dados\dbanco\SuperADM.txt', 'r')
    linhas = []
    for linha in arquivo:  # Percorrer arquivo linha por linha
        linhas.append(linha)  # Adicionar linha numa lista de linhas
    arquivo.close()
    posicao = adm_existe(cpf, linhas)
    if posicao is None:#Se não for encontrado, retornar mensagem de erro
        print('Usuário não encontrado')
    else:#Caso seja encontrado, retornar a senha
        valores = linhas[posicao].split(' ')
        senha = valores[len(valores) - 1]#pegando a senha
        senha = senha[:-1]#removendo o \n
        return senha