
import os #para ajudar com o caminho dos arquivos

caminho_arquivo = "ler_escrever_documentos/dados.txt"
#Acrescentar conteúdo sem apagar o que já existe
with open(caminho_arquivo, "a") as arquivo:
    arquivo.write("Mais uma linha adicionada\n")
    print("Arquivo:", arquivo.name)
    print("Gravou em:", os.path.abspath(arquivo.name))

with open(caminho_arquivo, "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)