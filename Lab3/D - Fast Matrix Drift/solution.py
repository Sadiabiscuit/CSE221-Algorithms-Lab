def matrix_multiply(matA, matB):
  mod = 10**9 + 7
  a11 = (matA[0][0]*matB[0][0] + matA[0][1]*matB[1][0]) % mod
  a12 = (matA[0][0]*matB[0][1] + matA[0][1]*matB[1][1]) % mod
  a21 = (matA[1][0]*matB[0][0] + matA[1][1]*matB[1][0]) % mod
  a22 = (matA[1][0]*matB[0][1] + matA[1][1]*matB[1][1]) % mod
  new = [[a11, a12], [a21, a22]]
  return new

t = int(input())
for i in range(t):
  arr = list(map(int, input().split()))
  N = int(input())
  mat = [arr[:2], arr[2:len(arr)]]
  res = [[1,0],[0,1]]
  while N > 0:
    if N%2 == 1:
      res = matrix_multiply(mat, res)
    mat = matrix_multiply(mat, mat)
    N = N // 2

  print(*res[0])
  print(*res[1])

