n = int(input())
arr = list(map(int, input().split()))

def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]
def checkarr(arr, n):
  for i in range(n-1):
    if arr[i] > arr[i+1]:
      return False

if n < 3:
  if n == 1:
    print("YES")
  elif n == 2:
    if arr[0] > arr[1]:
      print("NO")
    else:
      print("YES")
else:
   for i in range(n):
    for j in range(n-2):
      if arr[j] > arr[j+1]: 
        swap(arr, j, j+2)
      elif arr[j] > arr[j+2]:
        swap(arr, j, j+2)
   if checkarr(arr, n) == False:
    print("NO")
   else:
    print("YES")

 
