class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visit = set()
        path = set()
        print(adj_list)

        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)          
            for nei_node in adj_list[node]:
                if nei_node == parent:
                    continue  
                    
                if not dfs(nei_node, node):
                    return False
                    
            return True


        return dfs(0, visit) and len(visit) == n            

