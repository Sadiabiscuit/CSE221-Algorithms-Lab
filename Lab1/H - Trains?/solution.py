n = int(input())
lst = []
for i in range(n):
  store = input()
  st = store.split()
  lst.append([st[0], st[-1], store])
for i in range(n):
  for j in range(n - i - 1):
    if lst[j][0] > lst[j+1][0]:
      lst[j], lst[j+1] = lst[j+1], lst[j]
    elif lst[j][0] == lst[j + 1][0]:
      time1 = list(map(int, lst[j][1].split(":")))
      time2 = list(map(int, lst[j+1][1].split(":")))
      if time1[0] < time2[0]:
        lst[j], lst[j+1] = lst[j+1], lst[j]
      elif time1[0] == time2[0]:
        if time1[1] < time2[1]:
          lst[j], lst[j+1] = lst[j+1], lst[j]
      
for i in lst:
  print(i[2])
     
