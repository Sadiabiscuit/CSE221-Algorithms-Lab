n = int(input())
for i in range(n):
  inp = input().split()
  a = inp[1]
  s = inp[2]
  b = inp[3]
  if s == "+":
    res = float(a) + float(b)
  elif s == "-":
    res = float(a) - float(b)
  elif s == "*":
    res = float(a) * float(b)
  else:
    res = float(a) / float(b)
  print("%.6f"% res)
