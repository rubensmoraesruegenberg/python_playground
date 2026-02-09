from aula7 import somar, saudacao

def testar_soma():
    resultado = somar(2, 3)
    print(f"Testando soma: 2 + 3 = {resultado}")

def testar_saudacao():
    resultado = saudacao("Rubens")
    print(f"Testando saudação: {resultado}")

# Chamando os testes manualmente
testar_soma()
testar_saudacao()
