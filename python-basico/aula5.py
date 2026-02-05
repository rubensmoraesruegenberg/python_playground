nomes = ["Rubens", "Ana", "Carlos"]

print(nomes[0])  # Rubens
print(nomes[1])  # Ana

#percorrendo a lista
for nome in nomes:
    print(nome)

#adicionar item
nomes.append("Marcos")

for nome in nomes:
    print(nome)

#tamanho
print("tamanho do coleção")
print(len(nomes))


#exemplo com todas as opções
# Aula 5 - Listas

nomes = []

while True:
    nome = input("Digite um nome (ou 'sair'): ")

    if nome.lower() == "sair":
        break

    nomes.append(nome)

print("\nLista de nomes:")
for nome in nomes:
    print("-", nome)

#exercício

numeros = []

while True:
    numero = float(input("Digite um numero ou 0 para exibir dados da lista"))

    if(numero == 0):
        break
    numeros.append(numero)

print("Todos os números")
for numero in numeros:
    print("-", numero)

print("Maior número",max(numeros))


print("Menor número", min(numeros))


print("Média", sum(numeros)/len(numeros))
