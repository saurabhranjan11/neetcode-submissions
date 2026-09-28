class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cnt  = n
        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]
        def union(a,b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa
                return 1
            return 0
       
        for u, v in edges:
            cnt -= union(u,v)
        return cnt
        