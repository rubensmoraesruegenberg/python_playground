import pytest

from aula7 import somar, saudacao


#teste com falha
def test_falha():
    #assert somar(2, 2) == 5  # propositalmente errado
    assert somar(2, 2) == 4  # propositalmente ficar certo

#- Testes parametrizados (rodar várias entradas de uma vez):
@pytest.mark.parametrize("a,b,resultado", [
    (2, 3, 5),
    (-1, 1, 0),
    (10, -5, 5)
])
def test_soma_parametrizada(a, b, resultado):
    assert somar(a, b) == resultado

#para debugar linha a linha precisa chamar os testes manualmente.
# Chamando os testes manualmente

test_falha()
test_soma_parametrizada(2, 3, 5)
test_soma_parametrizada(-1, 1, 0)
test_soma_parametrizada(10, -5, 5)


