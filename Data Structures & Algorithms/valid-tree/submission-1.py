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
        components = 0

        for node in range(n):
            if node not in visit:
                components += 1
                if not dfs(node, None) or components > 1:
                    return False

        return components == 1