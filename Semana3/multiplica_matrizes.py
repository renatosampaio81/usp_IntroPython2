def mat_mul (A, B):
  num_lin_A = len(A)
  num_lin_B = len(B)
  num_col_A = len(A[0])
  num_col_B = len(B[0])
  assert num_col_A == num_lin_B #Pra multiplicar as matrizes é necessário essa verificação

  C = []

  for lin in range(num_lin_A):
    C.append([]) #linha vazia
    for col in range(num_col_B):
      C[lin].append(0) #adicionada coluna com valor 0
      for k in range(num_col_A):
        C[lin][col] += A[lin][k] * B[k][col]

  return C


if __name__ == '__main__':
  A = [[1,2,3], [4,5,6]]
  B = [[1,2], [3,4], [5,6]]
  print(mat_mul(A, B))
