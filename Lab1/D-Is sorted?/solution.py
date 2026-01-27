T = int(input())
for i in range(T):
  num = int(input())
  arr = list(map(int, input().split()))
  flag = False
  for j in range(num-1):
    if arr[j] > arr[j+1]:
      print("NO")
      flag = True
      break
  if flag is False:
    print("YES")

