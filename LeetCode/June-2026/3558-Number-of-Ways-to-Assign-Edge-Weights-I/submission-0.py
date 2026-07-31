class Solution:
    MOD = 10**9 + 7
    
    def dfs(self, adj, node, parent):
        depth = 0
        for child in adj[node]:
            if child == parent:
                continue
            depth = max(depth, 1+self.dfs(adj, child, node))

        return depth

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n+1)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        depth = self.dfs(adj, 1, -1)

        res = 1
        for _ in range(1, depth):
            res = (res * 2) % self.MOD

        return res
    


# Time Complexity: O(n)
# Space Complexity: O(n)
'''
The idea is to first build an adjacency list representation of the tree from the given edges. 
Then we perform a depth-first search (DFS) to find the maximum depth of the tree.
The maximum depth of the tree will determine the number of ways to assign edge weights.
If the maximum depth is d, then we can assign weights to the edges in 2^(d-1) ways, 
since we can choose to assign a weight of 1 or 2 to each edge at each level of the tree.
Finally, we return the result modulo 10^9 + 7 to handle large numbers.
'''