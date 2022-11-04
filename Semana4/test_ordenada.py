import lista_ordenada
import pytest

class TestOrdem:
  
  '''
  @pytest.fixture
  def o(self):
    return lista_ordenada

  def test_Ordem1(self, o):
    assert o.ordenada([3, 5, 8, 1, 2, 10]) == False

  def test_Ordem2(self, o):
    assert o.ordenada([3, 5, 8, 10, 12, 14]) == True

  def test_Ordem3(self, o):
    assert o.ordenada(['ave', 'frango', 'peixe', 'porco']) == True
  '''

  @pytest.mark.parametrize("entrada, saida", [
    ([3, 5, 8, 1, 2, 10], (False)),
    ([3, 5, 8, 10, 12, 14], (True)),
    (['ave', 'frango', 'peixe', 'porco'], (True)),
    (['porco', 'peixe', 'frango', 'ave'], (False))
  ])

  def test_Ordem4(self, entrada, saida):
    assert lista_ordenada.ordenada(entrada) == saida