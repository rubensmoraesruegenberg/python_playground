import csv
import json

caminho_arquivo_dados_csv = "ler_escrever_documentos/dados.csv"
caminho_arquivo_json = "ler_escrever_documentos/dados_csv.json"
caminho_arquivo_csv = "ler_escrever_documentos/dados_convertidos.csv"

# Lendo CSV e convertendo para JSON
with open(caminho_arquivo_dados_csv, "r") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    dados = list(leitor)

with open(caminho_arquivo_json, "w") as arquivo_json:
    json.dump(dados, arquivo_json, indent=4)

# Lendo JSON e convertendo para CSV
with open(caminho_arquivo_json, "r") as arquivo_json:
    dados_lidos = json.load(arquivo_json)

with open(caminho_arquivo_csv, "w", newline="") as arquivo_csv:
    campos = dados_lidos[0].keys()
    escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(dados_lidos)