import bisect
def count_inversions(N, A):
    sarr = []
    count = 0
    for j in range(N):
        square = A[j] ** 2
        idx = bisect.bisect_right(sarr, square)
        count += len(sarr) - idx
        bisect.insort(sarr, A[j])
    return count

n = int(input())
arr = list(map(int, input().split()))
result = count_inversions(n, arr)
print(result)
