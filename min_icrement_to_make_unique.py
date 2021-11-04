# O(NlogN) solution - sort and compare consequtive numbers

def minIncrementForUnique(self, A):
    res = need = 0
    for i in sorted(A):
        res += max(need - i, 0)
        need = max(need + 1, i + 1)
    return res
    
# O(N) - Union find

def minIncrementForUnique(self, A):
    root = {}
    def find(x):
        root[x] = find(root[x] + 1) if x in root else x
        return root[x]
    return sum(find(a) - a for a in A)
