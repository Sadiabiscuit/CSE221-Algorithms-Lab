def power(a, n, m):
  res = 1
  while n > 0:
    if n%2 == 1:
      res = (res*a) % m
    a = (a**2) % m
    n = n // 2
  return res
t = int(input())
for i in range(t):
  a, n, m = map(int, input().split())
  sum = 0
  if a == 1:
    sum = n 
  else:
    num = (power(a, n, m * (a - 1)) - 1) % (m * (a - 1))
    sum = (a * num) // (a - 1) 
  print(sum % m)
