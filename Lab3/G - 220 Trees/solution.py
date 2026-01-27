def postO(inO, preO):
    if len(preO) == 0:
      return []
    root = preO[0]
    ind = inO.index(root)
    left = postO(inO[:ind], preO[1:1+ind])
    right = postO(inO[ind+1:], preO[1+ind:])
    return left + right + [root]
    
n = int(input())
inO = list(map(int, input().split()))
preO = list(map(int, input().split()))
result = postO(inO, preO)
print(*result)
