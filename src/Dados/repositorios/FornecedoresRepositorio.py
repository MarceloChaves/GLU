from Entidades import Fornecedores


def fornecedor_existe(cnpj,linhas):
    posicao = None
    for x in range(0, len(linhas)):
        valores_separados = linhas[x].split(' ')
        if cnpj == valores_separados[0]:  # verifica se o cnpj é igual ao cnpj no arquivo
            posicao = x
    return posicao

def adicionar_Fornecedor(fornecedores):
    arquivo = open('..\Dados\dbanco\Fornecedores.txt', 'r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    posicao = fornecedor_existe(fornecedores.getCnpj(),linhas)
    arquivo.close()
    if posicao is None:#Se o fornecedores não existir no arquivo, inserir normalmente
        arquivo = open('..\Dados\dbanco\Fornecedores.txt', 'r')
        conteudo = arquivo.readlines()#recebe o conteúdo do arquivo
        conteudo.append(fornecedores.getCnpj() + ' ' + fornecedores.getNome() + fornecedores.getSenha()+'\n')#insere o conteúdo novo
        arquivo = open('..\Dados\dbanco\Fornecedores.txt', 'w')
        arquivo.writelines(conteudo)  #escreve no arquivo
        arquivo.close()
        return 'Cadastrado com sucesso'
    else:
        return 'Fornecedor já existe'

def limpar_Arquivo():
    arquivo = open('..\Dados\dbanco\Fornecedores.txt', 'w')
    arquivo.close()
def deletar_Fornecedor(cnpj):
    arquivo = open('..\Dados\dbanco\Fornecedores.txt','r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    arquivo.close()
    posicao = fornecedor_existe(cnpj,linhas)
    if posicao is None:
        return 'Fornecedor não encontrado'#Não encontrou o Fornecedor dentro do arquivo
    else:#Encontrou o Fornecedor dentro do arquivo e irá deleta-lo
        linhas.pop(posicao)#Deleta o fornecedo encontrado
        arquivo = open('..\Dados\dbanco\Fornecedores.txt', 'w')
        arquivo.writelines(linhas)#escreve novamente no arquivo
        arquivo.close()
        return 'Deletado com Sucesso'


def alterar_Fornecedor(fornecedores):
    arquivo = open('..\Dados\dbanco\Funcionario.txt', 'r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    arquivo.close()
    posicao = fornecedor_existe(fornecedores.getCnpj(),linhas)
    if posicao is None:  # Se o fornecedores não existir no arquivo, alteração não funciona
        return "Fornecedor não encontrado"
    else:#Se o funcionario existe, alterar normalmente
        arquivo = open('..\Dados\dbanco\Fornecedores.txt', 'r')
        conteudo = arquivo.readlines()  # recebe o conteúdo do arquivo
        conteudo[posicao] = fornecedores.getCnpj() + ' ' + fornecedores.getNome() +' ' + fornecedores.getSenha() + '\n'#Alterando o fornecedor encontrado
        arquivo = open('..\Dados\dbanco\Fornecedores.txt', 'w')
        arquivo.writelines(conteudo)#Escrevendo no arquivo
        arquivo.close()
        return 'Fornecedores atualizado com sucesso'

def buscar_Fornecedor(cnpj):
    arquivo = open('..\Dados\dbanco\Fornecedores.txt','r')
    linhas = []
    for linha in arquivo:#Percorrer arquivo linha por linha
        linhas.append(linha)#Adicionar linha numa lista de linhas
    arquivo.close()
    posicao = fornecedor_existe(cnpj,linhas)
    if posicao is None:#Se não for encontrado, retornar mensagem de erro
        return 'Usuário não encontrado'
    else:#Caso seja encontrado, retornar um objeto Funcionario
        nome = pegar_nome(linhas[posicao])
        valores = linhas[posicao].split(' ')
        obj = Fornecedores.Fornecedor(valores[0], nome, valores[len(valores) - 2])#instanciando objeto com cnpj, nome
        return obj#retornando objeto correspondente a busca

def listar_Fornecedores():
    arquivo = open('..\Dados\dbanco\Fornecedores.txt','r')
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

def pegar_senha(cnpj):
    arquivo = open('..\Dados\dbanco\FFornecedores.txt', 'r')
    linhas = []
    for linha in arquivo:  # Percorrer arquivo linha por linha
        linhas.append(linha)  # Adicionar linha numa lista de linhas
    arquivo.close()
    posicao = fornecedor_existe(cnpj, linhas)
    if posicao is None:#Se não for encontrado, retornar mensagem de erro
        print('Usuário não encontrado')
    else:#Caso seja encontrado, retornar a senha
        valores = linhas[posicao].split(' ')
        senha = valores[len(valores) - 1]#pegando a senha
        senha = senha[:-1]#removendo o \n
        return senha