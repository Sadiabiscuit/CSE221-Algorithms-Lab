t = int(input())
for i in range(t):
  k, x = map(int, input().split())
  div = k // (x-1)
  rem = k % (x-1)
  if rem == 0:
    print(div * x - 1)
  else:
    print(div * x + rem)
