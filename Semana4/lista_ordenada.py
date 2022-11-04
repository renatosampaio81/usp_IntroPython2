'''
Exercício 1: Lista ordenada

Escreva a função ordenada(lista), que recebe uma lista com números inteiros como parâmetro
e devolve o booleano True se a lista estiver ordenada e False se a lista não estiver ordenada.
'''

def ordenada(lista):
  original = lista[:]
  fim = len(lista)
  for i in range(fim - 1):
    posicao_do_minimo = i
    for j in range(i+1, fim):
      if lista[j] < lista[posicao_do_minimo]:
        posicao_do_minimo = j
    lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
  if lista == original:
    return True
  return False

'''
if __name__ == '__main__':
  #lista = [3, 5, 8, 1, 2, 10]
  lista = [3, 5, 8, 10, 12, 14]
  print(ordenada(lista))
'''