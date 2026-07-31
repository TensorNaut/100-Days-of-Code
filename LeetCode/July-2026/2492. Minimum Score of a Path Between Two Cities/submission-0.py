class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = list(range(n+1))
        rank = [0] * (n+1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)

            if pa == pb:
                return

            if rank[pa] < rank[pb]:
                parent[pa] = pb
            elif rank[pa] > rank[pb]:
                parent[pb] = pa
            else:
                parent[pb] = pa
                rank[pa] += 1
        
        for u, v, _ in roads:
            union(u, v)

        root = find(1)
        ans = float("inf")

        for u, v, d in roads:
            if find(u) == root:
                ans = min(ans, d)
        
        return ans


#Time Complexity: O(n + m * α(n)), where n is the number of cities, m is the number of roads, and α is the inverse Ackermann function. The union-find operations are nearly constant time.
#Space Complexity: O(n), for storing the parent and rank arrays.
'''
Approach:
1.  We use the Union-Find (Disjoint Set Union) data structure to group cities that are connected by roads.
    Each city starts as its own parent, and we union cities that are directly connected by a road.

2.  After processing all roads, we find the root of city 1. This root represents the connected component that 
    includes city 1.

3.  We then iterate through all the roads again, and for each road, we check if either of its cities belongs to 
    the same connected component as city 1 (i.e., has the same root).

4.  If a road connects to the same component as city 1, we consider its distance and keep track of the minimum 
    distance found.

5. Finally, we return the minimum distance found among all roads that connect to the same component as city 1.
'''