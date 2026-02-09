import csv

caminho_arquivo = "ler_escrever_documentos/dados.csv"
# Ler CSV
with open(caminho_arquivo, "r") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    alunos = list(leitor)

# Filtrar alunos de Engenharia
engenharia = [a for a in alunos if a["curso"] == "Engenharia"]

print("Alunos de Engenharia:")
for aluno in engenharia:
    print(f"{aluno['nome']} - {aluno['idade']} anos")

# Contar alunos por curso
cursos = {}
for aluno in alunos:
    curso = aluno["curso"]
    cursos[curso] = cursos.get(curso, 0) + 1

print("\nQuantidade de alunos por curso:")
for curso, qtd in cursos.items():
    print(f"{curso}: {qtd}")
