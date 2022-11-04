import busca_binaria
import pytest
import ContaTempo_1
import time

class Testa_Busca:

  #'''
  @pytest.fixture
  def b(self):
    return busca_binaria
  
  @pytest.fixture
  def l_ordenada(self):
    c = ContaTempo_1.ContaTempo_1()
    return c.lista_ordenada(2000)

  def test_bb1(self, b):
    assert b.busca(['a', 'e', 'i'], 'e') == 1

  def test_bb2(self, b):
    assert b.busca([12, 13, 14], 15) == False

  def test_bb3(self, b):
    assert b.busca(['ave', 'frango', 'peixe', 'porco'], 'porco') == 3

  def test_bb4(self, b, l_ordenada):
    assert b.busca(l_ordenada, 6) == 6
  #'''

  '''
  @pytest.mark.parametrize("entrada, saida", [
    ((['a', 'e', 'i'], 'e'), (1)),
    (([12, 13, 14], 15), (False)),
    ((['ave', 'frango', 'peixe', 'porco'], 'ave'), (0)),
    ((['ave', 'frango', 'peixe', 'porco'], 'porco'), (3))
  ])

  def testaBB(self, entrada, saida):
    assert busca_binaria.busca(entrada[0], entrada[1]) == saida
  '''

if __name__ == '__main__':
  c = ContaTempo_1.ContaTempo_1()
  qde = 5000
  resultado = c.lista_quase_ordenada(qde)
  print (resultado)
  print (resultado[0][qde//10])
  print ('verificando se -500 está contido no array resultado[0], na posicao resultado[1]....')
  if busca_binaria.busca(resultado[0], -500) == resultado[1]:
    print ('localizado !')
  else:
    print ('não localizado !')
  #assert busca_binaria.busca(resultado[0], -500) == resultado[1]
  #print ('localizado !')