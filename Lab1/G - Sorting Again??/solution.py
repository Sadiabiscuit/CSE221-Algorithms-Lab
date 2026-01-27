n = int(input())
id = list(map(int, input().split()))
mark = list(map(int, input().split()))
c = 0
for i in range(n):
  max = i
  flag = False
  for j in range(i+1, n):
    if mark[j] > mark[max]:
      max = j
      flag = True
    elif mark[j] == mark[max]:
      if id[j] < id[max]:
        max = j
        flag = True
  if flag is True:
    id[i], id[max] = id[max], id[i]
    mark[i], mark[max] = mark[max], mark[i]
    c +=1
print(f"Minimum swaps: {c}")

for i in range(n):
   print(f"ID: {id[i]} Mark: {mark[i]}")
