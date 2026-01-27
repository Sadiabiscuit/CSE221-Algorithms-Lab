n, key = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
right = n-1
flag = False
while left < right:
  sum = arr[left] + arr[right]
  if sum < key:
    left += 1
  elif sum > key:
    right -= 1
  else:
    print(left+1, right+1)
    flag = True
    break
if flag is False:
  print(-1)
