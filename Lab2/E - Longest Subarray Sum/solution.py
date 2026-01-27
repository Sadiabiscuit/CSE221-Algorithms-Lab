n, k = map(int, input().split())
arr = list(map(int, input().split()))

l = r = 0
p_sum = 0
length = 0

while l < n and r < n:
  p_sum += arr[r]
  if p_sum <= k:
    length = max(length, r - l + 1)
    r += 1
  else:
    p_sum -= arr[l]
    l+= 1
    r += 1

print(length)
