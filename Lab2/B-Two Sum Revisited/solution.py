  n, m, k = map(int, input().split())
  arr1 = list(map(int, input().split()))
  arr2 = list(map(int, input().split()))
  i, j = 0, m-1
  min = abs(arr1[0] + arr2[0] - k)
  a1, a2 = 1, 1
  while i <= n-1  and j >=0:
  
    sum = arr1[i] + arr2[j]
    diff = abs(sum - k)

    if diff < min:
      min = diff
      a1, a2 = i+1, j+1
    if sum == k:
      a1, a2 = i+1, j+1
      break
    elif sum < k:
      i = i+1
    else:
      j = j-1

  print(a1, a2)



