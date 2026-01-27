n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n):
  k = arr[i]
  j = i - 1
  while j >= 0 and arr[j] > k and arr[j]%2 == 0 and arr[j+1]%2 == 0:
     arr[j+1] = arr[j]
     j = j -1
  arr[j + 1 ] = k
  while j >= 0 and arr[j] > k and arr[j]%2 != 0 and arr[j+1]%2 != 0:
     arr[j+1] = arr[j]
     j = j -1
  arr[j + 1 ] = k
  
print(*arr)
