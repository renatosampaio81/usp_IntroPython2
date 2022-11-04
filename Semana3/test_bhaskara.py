'''
import Bhaskara

class TestBhaskara:

    def testa_uma_raiz(self):
        b = Bhaskara.Bhaskara()
        assert b.calcula_raizes(1, 0, 0) == (1, 0)
        
    def testa_duas_raiz(self):
        b = Bhaskara.Bhaskara()
        assert b.calcula_raizes(1, -5, 6) == (2, 3, 2)
        
    def testa_zero_raiz(self):
        b = Bhaskara.Bhaskara()
        assert b.calcula_raizes(10, 10, 10) == (0)
        
    def testa_raiz_negativa(self):
        b = Bhaskara.Bhaskara()
        assert b.calcula_raizes(10, 20, 10) == (1, -1)
'''

#o código abaixo está aprimorado. Ele utiliza Fixtures, que é um valor fixo para um conjunto de testes
import Bhaskara
import pytest #necessário para utilizar fixtures

class TestBhaskara:
    
    #A função b, quando chamada, vai retornar Bhaskara.Bhaskara()
    @pytest.fixture
    def b(self):
        return Bhaskara.Bhaskara()
  
    def testa_uma_raiz(self, b):
        assert b.calcula_raizes(1, 0, 0) == (1, 0)
        
    def testa_duas_raiz(self, b):
        assert b.calcula_raizes(1, -5, 6) == (2, 3, 2)
        
    def testa_zero_raiz(self, b):
        assert b.calcula_raizes(10, 10, 10) == (0)
        
    def testa_raiz_negativa(self, b):
        assert b.calcula_raizes(10, 20, 10) == (1, -1)
