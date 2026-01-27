def merge(a, b):
  i=j=0
  lst = []
  count = 0
  while i < len(a) and j < len(b):
    if a[i] < b[j]:
      lst.append(a[i])
      i+=1
    else:
      lst.append(b[j])
      count += len(a) - i
      j+=1
  
  lst.extend(a[i:])
  lst.extend(b[j:])
  return lst, count
def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr)//2
    a1, leftcount = mergeSort(arr[:mid:])   
    a2, rightcount = mergeSort(arr[mid::])  
    result, inversion = merge(a1, a2)

    total = leftcount + rightcount + inversion
    return result, total   
n = int(input())
arr = list(map(int, input().split()))
sarr, inv = mergeSort(arr)
print(inv)
print(*sarr)
