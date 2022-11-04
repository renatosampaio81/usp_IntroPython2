import tipo_triangulo
import pytest

class TestClasseTri:
  
  @pytest.fixture
  def c(self):
    return tipo_triangulo

  def test_Tri2(self, c):
    objeto = c.Triangulo(1, 1, 1)
    assert objeto.tipo_lado() == 'equilátero'

  def test_Tri3(self, c):
    objeto = c.Triangulo(2, 1, 1)
    assert objeto.tipo_lado() == 'isósceles'

  def test_Tri4(self, c):
    objeto = c.Triangulo(2, 1, 3)
    assert objeto.tipo_lado() == 'escaleno'

  '''
  @pytest.mark.parametrize("entrada, saida", [
    ((10, 10, 10), ('equilátero')),
    ((20, 22, 22), ('isósceles')),
    ((30, 22, 12), ('escaleno')),
  ])

  def test_Tri(self, entrada, saida):
    objeto = tipo_triangulo.Triangulo(entrada[0],entrada[1], entrada[2])
    assert objeto.tipo_lado() == saida
  '''