import cria_matriz

def soma_matrizes (A, B):
  num_lin = len(A)
  num_col = len(A[0])
  C = cria_matriz.cria_matriz(num_lin, num_col, 0)

  for lin in range(num_lin):
    for col in range(num_col):
      C[lin][col] = A[lin][col] + B[lin][col]
  return C

if __name__ == '__main__':
  A = [[1,1,1], [2,2,2], [3,3,3]]
  B = [[1,1,1], [2,2,2], [3,3,3]]
  print(soma_matrizes(A, B))
