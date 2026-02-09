import json

# Dados de exemplo (um dicionário com informações)
dados = {
    "nome": "Rubens",
    "curso": "Python Avançado",
    "progresso": 85
}

caminho_arquivo = "ler_escrever_documentos/dados.json"

# Salva os dados em um arquivo JSON
with open(caminho_arquivo, "w") as arquivo_json:
    json.dump(dados, arquivo_json, indent=4)  # 'indent' para formatação bonita

# Agora vamos ler de volta esse JSON
with open(caminho_arquivo, "r") as arquivo_json:
    dados_lidos = json.load(arquivo_json)
    print("Dados lidos:", dados_lidos)
