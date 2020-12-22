
def escrever_arquivo(texto):
    diretorio = 'C:/Users/henri/OneDrive/Documentos/PycharmProjects/pythonProject/teste.txt'
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    #escrever_arquivo('Primeira linha.\n')
    #atualizar_arquivo('Quarta linha\n')
    ler_arquivo('teste.txt')