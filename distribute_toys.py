# toy in a sitting compile
# distribute k toys among n people starting at i

def distributeToys(n,k,i):
  k = k % n
  if i-1 + k > n:
    return i-1 + k - n
  else:
    return i-1 + k

ans = distributeToys(6, 10, 5)
print(ans)
