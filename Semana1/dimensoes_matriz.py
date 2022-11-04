'''Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e 
imprime as dimensões da matriz recebida, no formato iXj. '''

def dimensoes(matriz):
  tamLin = len(matriz)
  tamCol = len(matriz[0])
  return print(tamLin,'X',tamCol, sep="")


'''
if __name__ == '__main__':
  minha_matriz = [[1, 2, 3], [4, 5, 6]]
  dimensoes(minha_matriz)
'''