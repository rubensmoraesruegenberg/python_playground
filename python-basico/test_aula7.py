from aula7 import somar, saudacao

def test_soma():
    resultado = somar(2, 3)
    print(f"Testando soma: 2 + 3 = {resultado}")

def test_saudacao():
    resultado = saudacao("Rubens")
    print(f"Testando saudação: {resultado}")

# para debugar precisa chamar o teste em algum lugar,
# e eles ficando aqui, não atrapaha o pytest -v
test_soma()
test_saudacao()
# Chamando os testes manualmente
#test_soma()
#test_saudacao()
