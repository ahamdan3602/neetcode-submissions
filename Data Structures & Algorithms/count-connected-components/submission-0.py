from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = defaultdict(list)

        for u, v in edges:
            mp[u].append(v)
            mp[v].append(u)

        path = set()
        visit = set()

        cnt = 0
        def dfs(node):
            if node in visit:
                return
            visit.add(node)

            for nei_node in mp[node]:
                dfs(nei_node)
            

        for node in range(n):
            if node not in visit:
                dfs(node)
                cnt += 1
        return cnt

        


            