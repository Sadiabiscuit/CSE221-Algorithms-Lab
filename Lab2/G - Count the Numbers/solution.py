n, q = map(int, input().split())
arr = list(map(int, input().split()))
def helper(arr, n, target):
  left = 0
  right = n - 1
  ind = n
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] >= target:
      ind = mid
      right = mid - 1
    else:
      left = mid + 1
  return ind

for i in range(q):
  x, y = map(int, input().split())
  result = helper(arr, n, y+1) - helper(arr, n, x)
  print(result)
