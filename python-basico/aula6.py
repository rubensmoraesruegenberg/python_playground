# 1. Função que recebe uma lista de números e retorna a soma
def somar_lista(numeros):
    return sum(numeros)

# Testando a função
print(somar_lista([1, 2, 3, 4, 5]))  # Saída: 15


# 2. Função que recebe um dicionário e imprime chave/valor
def imprimir_dicionario(dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

# Testando a função
imprimir_dicionario({"nome": "Rubens", "idade": 30, "cidade": "São Paulo"})


# 3. Função que recebe nome e idade e retorna uma string formatada
def formatar_pessoa(nome, idade):
    return f"Nome: {nome}, Idade: {idade} anos"

# Testando a função
print(formatar_pessoa("Rubens", 30))