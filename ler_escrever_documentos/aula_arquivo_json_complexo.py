import json

# Lista de dicionários
alunos = [
    {"nome": "Ana", "idade": 20, "curso": "Engenharia"},
    {"nome": "Carlos", "idade": 22, "curso": "Direito"},
    {"nome": "Marina", "idade": 19, "curso": "Medicina"}
]

caminho_arquivo = "ler_escrever_documentos/alunos.json"

# Salvar em JSON
with open(caminho_arquivo, "w") as arquivo:
    json.dump(alunos, arquivo, indent=4)

# Ler de volta
with open(caminho_arquivo, "r") as arquivo:
    lista_lida = json.load(arquivo)

# Percorrer os dados
for aluno in lista_lida:
    print(f"{aluno['nome']} - {aluno['curso']}")