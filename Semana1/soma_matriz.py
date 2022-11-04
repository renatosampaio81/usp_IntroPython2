
def soma_matrizes(m1, m2):
  if(len(m1) != len(m2) or len(m1[0]) != len(m2[0])):
    return False
  soma = []
  for i in range(len(m1)):
    soma.append([])
    for j in range(len(m1[0])):
      soma[i].append(m1[i][j] + m2[i][j])
  return soma

'''
if __name__ == '__main__':
  m1 = [[1, 2, 3], [4, 5, 6]]
  #m1 = [[1], [2], [3]]
  m2 = [[2, 3, 4], [5, 6, 7]]
  soma_matrizes(m1, m2)
'''