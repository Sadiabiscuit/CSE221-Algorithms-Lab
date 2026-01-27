n = int(input())
arr = list(map(int, input().split()))
def balanceBST(arr, l, h):
  if l>h :
    return
  mid = (l+h)//2
  print(arr[mid], end = " ")
  balanceBST(arr, l, mid-1)
  balanceBST(arr, mid+1, h)

balanceBST(arr, 0, n-1)
