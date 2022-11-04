import classe_triangulo
import pytest

class TestClasseTri:
  
  '''
  @pytest.fixture
  def c(self):
    return classe_triangulo

  def test_Tri2(self, c):
    objeto = c.Triangulo(1, 1, 1)
    assert objeto.perimetro() == 3

  def test_Tri3(self, c):
    objeto = c.Triangulo(2, 2, 2)
    assert objeto.perimetro() == 6
  '''

  @pytest.mark.parametrize("entrada, saida", [
    ((1, 1, 1), (3)),
    ((2, 2, 2), (6))
  ])

  def test_Tri(self, entrada, saida):
    objeto = classe_triangulo.Triangulo(entrada[0],entrada[1], entrada[2])
    assert objeto.perimetro() == saida