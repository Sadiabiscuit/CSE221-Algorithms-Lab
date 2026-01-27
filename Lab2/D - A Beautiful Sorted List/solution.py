n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

p1 = 0
p2 = 0
final = []
while p1 < n and p2 <m:
  if arr1[p1] < arr2[p2]:
    final.append(arr1[p1])
    p1 += 1
  else:
    final.append(arr2[p2])
    p2 += 1

for i in range(p1,n):
  final.append(arr1[i])
for j in range(p2,m):
  final.append(arr2[j])

print(*final)
