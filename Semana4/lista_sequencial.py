'''
Exercício 2: Busca sequencial

Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e devolve o índice correspondente à posição do elemento encontrado.
Utilize o algoritmo de busca sequencial. Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False.
'''

def busca(lista, elemento):
  fim = len(lista)
  for i in range(fim):
    if lista[i] == elemento:
      return i
  return False


'''
if __name__ == '__main__':
  print(busca(['a', 'e', 'i'], 'e'))
  print(busca([12, 13, 14], 15))
'''