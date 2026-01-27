a, b = map(int, input().split())
mod = 107
sol = 1
while b > 0:
  if b % 2 == 1:
    sol = (sol * a) % mod
  b = b // 2
  a = (a**2) % mod

print(sol)
