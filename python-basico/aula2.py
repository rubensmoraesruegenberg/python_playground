# Aula 2 - Entrada de dados e conversão de tipos

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print("\nResumo:")
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)

print("Daqui a 10 anos, sua idade será:", idade + 10)

# Aula 2 - Exercício de fixação - verificar aumento de salário
print("Verifique o aumento de salário.")
nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite seu salário: "))
porcentagem = float(input("Digite o percentual do aumento: "))

print("novo salário = ", salario + ((salario * porcentagem)/ 100))
