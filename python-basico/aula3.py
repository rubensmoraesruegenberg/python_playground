# Aula 3 - Condicionais

#idade = int(input("Digite sua idade: "))

#if idade >= 18:
#    print("Você é maior de idade")
#else:
#    print("Você é menor de idade")



nota = float(input("Digite a nota: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")


salario = float(input("Digite o salário: "))
idade = int(input("Digite a idade: "))

if salario >= 3000 and idade >= 21:
    print("Crédito aprovado")
else:
    print("Crédito negado")