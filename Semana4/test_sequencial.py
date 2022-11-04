import lista_sequencial
import pytest

class TestSequencial:
  
  '''
  @pytest.fixture
  def s(self):
    return lista_sequencial

  def test_Sequencial1(self, s):
    assert s.busca(['a', 'e', 'i'], 'e') == 1

  def test_Sequencial2(self, s):
    assert s.busca([12, 13, 14], 15) == False

  def test_Sequencial3(self, s):
    assert s.busca(['ave', 'frango', 'peixe', 'porco'], 'porco') == 3
  '''

  #'''
  @pytest.mark.parametrize("entrada, saida", [
    ((['a', 'e', 'i'], 'e'), (1)),
    (([12, 13, 14], 15), (False)),
    ((['ave', 'frango', 'peixe', 'porco'], 'ave'), (0)),
    ((['ave', 'frango', 'peixe', 'porco'], 'porco'), (3))
  ])

  def test_Ordem4(self, entrada, saida):
    assert lista_sequencial.busca(entrada[0], entrada[1]) == saida
  #'''