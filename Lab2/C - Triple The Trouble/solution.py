n, target = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(n):
  arr[i] = (arr[i], i+1)
sarr = sorted(arr)
flag = False
for i in range(n):
  x = i
  y = i+1
  z = n-1
  new = target - sarr[x][0]
  while y<z:
    sum = sarr[y][0] + sarr[z][0]
    if sum == new:
      print(sarr[x][1], sarr[y][1], sarr[z][1])
      flag = True
      break
    elif sum < new:
      y = y+1
    else:
      z = z-1
  if flag is True:
    break
if flag is False:
  print(-1)
