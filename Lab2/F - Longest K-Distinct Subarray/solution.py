n, k = map(int, input().split())
arr = list(map(int, input().split()))

c_list = [0] * (n + 1)
l = 0
count = 0
length = 0

for i in range(n):
    val = arr[i]
    if c_list[val] == 0:
        count += 1
    c_list[val] += 1

    while count > k:
        temp = arr[l]
        c_list[temp] -= 1
        if c_list[temp] == 0:
            count -= 1
        l += 1

    length = max(length, i - l + 1)

print(length)
