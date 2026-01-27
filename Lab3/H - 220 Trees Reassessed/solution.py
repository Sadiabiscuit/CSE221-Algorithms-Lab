def preO(inO, postO): 
    if len(postO) == 0:
      return []
    root = postO[-1]
    ind = inO.index(root)
    left = preO(inO[:ind], postO[:ind])
    right = preO(inO[ind+1:], postO[ind:-1])
    return [root] + left + right
    
n = int(input())
inO = list(map(int, input().split()))
postO = list(map(int, input().split()))
result = preO(inO, postO)
print(*result)
